/* Envoy design-system enforcement.
 *
 *   node redesign/_system/check.mjs
 *
 * Serves the built page, drives headless Chrome, and fails (exit 1) if any law
 * is broken. build.py runs this and refuses to publish a page that fails.
 *
 *   1. every interactive control is >= 24x24, hit area included
 *   2. every interactive control has a visible hover change
 *   3. every interactive control has a focus ring
 *   4. every .btn resolves to its variant's token values — no local overrides
 *   5. no colour outside the palette appears on a system component
 */
import { spawn } from 'child_process';
import http from 'http';
import fs from 'fs';
import path from 'path';
import os from 'os';
import { fileURLToPath } from 'url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const DIR = path.join(HERE, '..', 'build');
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const sleep = ms => new Promise(r => setTimeout(r, ms));

const MIME = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.jpg': 'image/jpeg', '.png': 'image/png' };

// ---- the law, as values -----------------------------------------------------
const INK = 'rgb(12, 16, 36)', WHITE = 'rgb(255, 255, 255)';
const EXPECT = {
  'btn-primary':        { base: { backgroundColor: INK, color: WHITE }, hover: { backgroundColor: 'rgb(58, 52, 214)' } },
  'btn-secondary':      { base: { color: INK, borderColor: 'rgb(127, 132, 159)' }, hover: { borderColor: INK } },
  'btn-ghost':          { base: { color: 'rgb(72, 77, 107)' }, hover: { color: INK } },
  'btn-chip':           { base: { backgroundColor: WHITE, color: INK }, hover: { backgroundColor: 'rgb(201, 195, 255)' } },
  'on-dark btn-primary': { base: { backgroundColor: WHITE, color: INK }, hover: { backgroundColor: 'rgb(167, 155, 255)' } },
  'on-dark btn-secondary': { base: { color: WHITE, borderColor: 'rgba(255, 255, 255, 0.48)' }, hover: { borderColor: WHITE } },
  'on-dark btn-ghost':  { base: { color: 'rgb(198, 196, 222)' }, hover: { color: WHITE } },
};
const FOCUS_LIGHT = 'rgb(58, 52, 214)', FOCUS_DARK = 'rgb(167, 155, 255)';
const PALETTE = new Set([
  'rgb(12, 16, 36)', 'rgb(255, 255, 255)', 'rgb(72, 77, 107)', 'rgb(90, 95, 125)',
  'rgb(234, 236, 250)', 'rgb(244, 245, 252)', 'rgb(229, 231, 244)', 'rgb(210, 213, 234)',
  'rgb(127, 132, 159)', 'rgb(233, 232, 253)', 'rgb(201, 195, 255)', 'rgb(167, 155, 255)',
  'rgb(143, 134, 255)', 'rgb(58, 52, 214)', 'rgb(43, 38, 172)', 'rgb(25, 23, 53)',
  'rgb(198, 196, 222)', 'rgb(179, 174, 232)', 'rgba(0, 0, 0, 0)',
]);
const paletteOk = v => PALETTE.has(v) || /^rgba\(255, 255, 255, [\d.]+\)$/.test(v) || /^rgba\(12, 16, 36, [\d.]+\)$/.test(v);

// ---- plumbing ---------------------------------------------------------------
function serve() {
  return new Promise(res => {
    const srv = http.createServer((req, rep) => {
      const f = path.join(DIR, decodeURI(req.url.split('?')[0]) === '/' ? 'index.html' : decodeURI(req.url.split('?')[0]));
      fs.readFile(f, (e, b) => e ? (rep.statusCode = 404, rep.end('x'))
        : (rep.setHeader('content-type', MIME[path.extname(f)] || 'application/octet-stream'), rep.end(b)));
    });
    srv.listen(0, () => res({ srv, port: srv.address().port }));
  });
}
async function connect(port) {
  let t = null;
  for (let i = 0; i < 80 && !t; i++) {
    try { const j = await (await fetch(`http://127.0.0.1:${port}/json`)).json(); t = j.find(x => x.type === 'page'); } catch {}
    if (!t) await sleep(250);
  }
  const ws = new WebSocket(t.webSocketDebuggerUrl);
  await new Promise((r, j) => { ws.onopen = r; ws.onerror = j; });
  let id = 0; const pend = new Map();
  ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && pend.has(m.id)) { const p = pend.get(m.id); pend.delete(m.id); m.error ? p.rej(new Error(JSON.stringify(m.error))) : p.res(m.result); } };
  return { ws, send: (method, params = {}) => new Promise((res, rej) => { const i = ++id; pend.set(i, { res, rej }); ws.send(JSON.stringify({ id: i, method, params })); }) };
}

async function audit(view, w, h, dbg, url) {
  const prof = path.join(os.tmpdir(), 'envoy-check-' + dbg);
  const proc = spawn(CHROME, [`--remote-debugging-port=${dbg}`, `--user-data-dir=${prof}`, '--headless=new',
    '--no-first-run', '--no-default-browser-check', '--hide-scrollbars', `--window-size=${w},${h}`, 'about:blank'], { stdio: 'ignore' });
  const { ws, send } = await connect(dbg);
  await send('Page.enable'); await send('DOM.enable'); await send('CSS.enable');
  await send('Network.enable'); await send('Network.setCacheDisabled', { cacheDisabled: true });
  await send('Emulation.setDeviceMetricsOverride', { width: w, height: h, deviceScaleFactor: 1, mobile: w < 768 });
  await send('Page.navigate', { url }); await sleep(3500);
  const ev = async e => (await send('Runtime.evaluate', { expression: e, returnByValue: true })).result?.value;
  // freeze transitions so a forced state is read at its final value, not mid-flight
  await ev(`(function(){var st=document.createElement('style');
    st.textContent='*,*::before,*::after{transition:none !important;animation:none !important}';
    document.head.appendChild(st);})()`); await sleep(120);
  await ev(`(function(){var m=document.querySelector('${view} #m-menu-btn'); if(m) m.click();})()`); await sleep(250);

  const meta = JSON.parse(await ev(`(function(){
    var root=document.querySelector('${view}'), out=[];
    [].forEach.call(root.querySelectorAll('a,button,[role="button"],input,textarea,select'),function(e,i){
      e.setAttribute('data-chk',i);
      var r=e.getBoundingClientRect(), ps=getComputedStyle(e,'::after');
      var pw=parseFloat(ps.width), ph=parseFloat(ps.height), grow=false;
      if(ps.content && ps.content!=='none' && ps.position==='absolute' && pw>0 && ph>0){ grow=true; }
      var cl=(typeof e.className==='string'?e.className:'');
      out.push({i:i, tag:e.tagName, cls:cl,
        label:(e.getAttribute('aria-label')||e.textContent||e.placeholder||'').trim().replace(/\\s+/g,' ').slice(0,34),
        w:Math.round(grow?Math.max(r.width,pw):r.width), h:Math.round(grow?Math.max(r.height,ph):r.height),
        onDark: !!e.closest('.on-dark'),
        variant: ['btn-primary','btn-secondary','btn-ghost','btn-chip'].filter(function(v){return cl.split(' ').indexOf(v)>=0;})[0]||null,
        isBtn: cl.split(' ').indexOf('btn')>=0 || cl.split(' ').indexOf('btn-icon')>=0});
    });
    return JSON.stringify(out);})()`));

  const { root } = await send('DOM.getDocument', { depth: -1 });
  const read = async i => await ev(`(function(e){
     function g(el,pe){var c=getComputedStyle(el,pe);return [c.backgroundColor,c.color,c.borderTopColor,c.boxShadow,
       c.opacity,c.transform,c.filter,c.width,c.height].join('|');}
     var c=getComputedStyle(e);
     return {backgroundColor:c.backgroundColor,color:c.color,borderColor:c.borderTopColor,
       outlineColor:c.outlineColor,outlineWidth:c.outlineWidth,outlineStyle:c.outlineStyle,
       boxShadow:c.boxShadow,transform:c.transform,opacity:c.opacity,filter:c.filter,
       self:g(e,null), before:g(e,'::before'), after:g(e,'::after')};
     })(document.querySelector('${view} [data-chk="${i}"]'))`);

  const bad = [];
  for (const m of meta) {
    if (m.w === 0 && m.h === 0) continue;                       // genuinely hidden right now
    const who = `${view === '.vd' ? 'desktop' : 'mobile'} · ${(m.cls || m.tag).slice(0, 24)} "${m.label.slice(0, 24)}"`;
    if (m.w < 24 || m.h < 24) bad.push(`TARGET  ${who} is ${m.w}x${m.h}, under 24x24`);

    const { nodeIds } = await send('DOM.querySelectorAll', { nodeId: root.nodeId, selector: `${view} [data-chk="${m.i}"]` });
    const id = nodeIds[0]; if (!id) continue;
    const base = await read(m.i);
    await send('CSS.forcePseudoState', { nodeId: id, forcedPseudoClasses: ['hover'] }); await sleep(20);
    const hov = await read(m.i);
    await send('CSS.forcePseudoState', { nodeId: id, forcedPseudoClasses: ['focus', 'focus-visible'] }); await sleep(20);
    const foc = await read(m.i);
    await send('CSS.forcePseudoState', { nodeId: id, forcedPseudoClasses: ['active'] }); await sleep(20);
    const act = await read(m.i);
    await send('CSS.forcePseudoState', { nodeId: id, forcedPseudoClasses: [] });

    const changed = (a, b) => ['self', 'before', 'after'].some(k => a[k] !== b[k]);
    const isField = m.tag === 'TEXTAREA' || m.tag === 'INPUT';
    if (!isField && !changed(base, hov)) bad.push(`HOVER   ${who} has no hover change`);
    if (!isField && foc.outlineStyle === 'none') bad.push(`FOCUS   ${who} has no focus ring`);
    if (!isField && foc.outlineStyle !== 'none') {
      const want = m.onDark ? FOCUS_DARK : FOCUS_LIGHT;
      if (foc.outlineColor !== want) bad.push(`FOCUS   ${who} ring is ${foc.outlineColor}, expected ${want}`);
    }
    if (m.isBtn && m.variant) {
      const key = (m.onDark ? 'on-dark ' : '') + m.variant;
      const spec = EXPECT[key] || EXPECT[m.variant];
      if (spec) {
        for (const [k, v] of Object.entries(spec.base)) if (base[k] !== v) bad.push(`TOKEN   ${who} ${key} ${k} is ${base[k]}, law says ${v}`);
        for (const [k, v] of Object.entries(spec.hover || {})) if (hov[k] !== v) bad.push(`TOKEN   ${who} ${key} hover ${k} is ${hov[k]}, law says ${v}`);
      }
      if (act.transform === base.transform && act.boxShadow === base.boxShadow)
        bad.push(`PRESS   ${who} has no pressed state`);
    }
    if (m.isBtn) for (const k of ['backgroundColor', 'color', 'borderColor'])
      if (!paletteOk(base[k])) bad.push(`PALETTE ${who} ${k} ${base[k]} is not in the palette`);
  }
  ws.close(); proc.kill();
  return { bad, count: meta.filter(m => m.w || m.h).length };
}

const { srv, port } = await serve();
const url = `http://127.0.0.1:${port}/`;
const d = await audit('.vd', 1440, 900, 9941, url);
const m = await audit('.vm', 402, 874, 9943, url);
srv.close();
const all = [...d.bad, ...m.bad];
console.log(`design-system check — ${d.count} desktop + ${m.count} mobile controls`);
if (all.length) { console.log(`\n${all.length} VIOLATION(S):`); all.forEach(v => console.log('  ' + v)); process.exit(1); }
console.log('all laws hold.');
process.exit(0);
