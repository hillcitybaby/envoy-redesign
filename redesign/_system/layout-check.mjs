/* Layout laws, enforced at build time alongside the button laws.
 *
 *   6. no text is clipped by an ancestor at any tested width
 *   7. nothing extends past the viewport
 *   8. a reader's text-spacing settings (WCAG 1.4.12) cost no content
 *   9. no font-size or structural height is hard-coded outside the system
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
const WIDTHS = [320, 375, 768, 1024, 1440];
const SPACING_WIDTHS = [375, 1024];
const MIME = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.jpg': 'image/jpeg', '.png': 'image/png' };

const TEXT_SPACING = `*{line-height:1.5 !important;letter-spacing:0.12em !important;word-spacing:0.16em !important}
p{margin-bottom:2em !important}`;

const PROBE = `(function(){
  var DECOR=['marquee','marquee-track','ghost','sr','photo','stage','blob'];
  function decor(e){ while(e&&e!==document.body){ var c=(typeof e.className==='string'?e.className:'');
      for(var i=0;i<DECOR.length;i++) if((' '+c+' ').indexOf(' '+DECOR[i]+' ')>=0) return true;
      if(e.getAttribute&&e.getAttribute('aria-hidden')==='true') return true; e=e.parentElement;} return false; }
  function nm(e){var s=e.tagName.toLowerCase(); if(e.id)s+='#'+e.id;
    var c=(typeof e.className==='string'?e.className:'').trim(); if(c)s+='.'+c.split(/\\s+/).slice(0,2).join('.'); return s;}
  var view=getComputedStyle(document.querySelector('.vd')).display!=='none'?'.vd':'.vm';
  var root=document.querySelector(view), out=[];
  [].forEach.call(root.querySelectorAll('*'),function(e){
    var own=''; for(var i=0;i<e.childNodes.length;i++){var n=e.childNodes[i]; if(n.nodeType===3) own+=n.textContent;}
    if(!own.trim()||decor(e)) return;
    var r=e.getBoundingClientRect(); if(!r.width||!r.height) return;
    var p=e.parentElement, clip=null;
    while(p&&p!==document.documentElement){ var pc=getComputedStyle(p);
      if(pc.overflowX!=='visible'||pc.overflowY!=='visible'){clip=p;break;} p=p.parentElement; }
    var box=clip?clip.getBoundingClientRect():{left:0,top:0,right:innerWidth,bottom:1e9};
    if(Math.round(r.right-box.right)>1||Math.round(r.bottom-box.bottom)>1)
      out.push('CLIPPED "'+own.trim().slice(0,24)+'" in '+nm(e)+(clip?' by '+nm(clip):''));
    if(r.right>innerWidth+1) out.push('PAST VIEWPORT '+nm(e));
  });
  [].forEach.call(root.querySelectorAll('*'),function(e){
    var cs=getComputedStyle(e);
    var clips=(cs.overflowY==='hidden'||cs.overflowY==='clip'||cs.overflowX==='hidden'||cs.overflowX==='clip');
    if(clips && e.scrollHeight>e.clientHeight+2 && e.clientHeight>0 && !decor(e))
      out.push('CONTENT LOST '+nm(e)+' needs '+e.scrollHeight+', has '+e.clientHeight);
  });
  var u=[],seen={}; out.forEach(function(x){if(!seen[x]){seen[x]=1;u.push(x);}});
  return JSON.stringify(u);
})()`;

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

const bad = [];

// --- law 9: source scan -------------------------------------------------------
const html = fs.readFileSync(path.join(DIR, 'index.html'), 'utf8');
const css = html.slice(html.indexOf('<style>'), html.indexOf('</style>'))
  .replace(/\/\* ==ENVOY-SYSTEM:START== \*\/[\s\S]*?\/\* ==ENVOY-SYSTEM:END== \*\//g, '');
const KEEP = /(svg|::before|::after|\.go|\.btn-icon|\.menu-btn|\.sr|label|\.states|\.eyebrow i|\.art|\.tip)/;
for (const m of css.matchAll(/([^{}]+)\{([^{}]*)\}/g)) {
  const [, sel, body] = m;
  for (const f of body.matchAll(/(?<![-\w])font-size\s*:\s*([\d.]+)px/g))
    bad.push(`SCALE   ${sel.trim().slice(0, 40)} hard-codes font-size:${f[1]}px — use a --t-* step`);
  if (!KEEP.test(sel))
    for (const h of body.matchAll(/(?<![-\w])height\s*:\s*([\d.]+)px/g))
      bad.push(`HEIGHT  ${sel.trim().slice(0, 40)} hard-codes height:${h[1]}px — use min-height`);
}

// --- laws 6-8: runtime --------------------------------------------------------
const { srv, port } = await serve();
const prof = path.join(os.tmpdir(), 'envoy-check-layout');
const proc = spawn(CHROME, [`--remote-debugging-port=10021`, `--user-data-dir=${prof}`, '--headless=new',
  '--no-first-run', '--no-default-browser-check', '--hide-scrollbars', '--window-size=1440,900', 'about:blank'], { stdio: 'ignore' });
const { ws, send } = await connect(10021);
await send('Page.enable'); await send('Network.enable'); await send('Network.setCacheDisabled', { cacheDisabled: true });
await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
await send('Page.navigate', { url: `http://127.0.0.1:${port}/` }); await sleep(3200);
const ev = async e => (await send('Runtime.evaluate', { expression: e, returnByValue: true })).result?.value;

for (const w of WIDTHS) {
  await send('Emulation.setDeviceMetricsOverride', { width: w, height: 900, deviceScaleFactor: 1, mobile: w < 768 });
  await sleep(380);
  JSON.parse(await ev(PROBE)).forEach(x => bad.push(`${w}px   ${x}`));
}
for (const w of SPACING_WIDTHS) {
  await send('Emulation.setDeviceMetricsOverride', { width: w, height: 900, deviceScaleFactor: 1, mobile: w < 768 });
  await sleep(300);
  await ev(`(function(){var s=document.createElement('style');s.id='ts';s.textContent=${JSON.stringify(TEXT_SPACING)};document.head.appendChild(s);})()`);
  await sleep(380);
  JSON.parse(await ev(PROBE)).forEach(x => bad.push(`${w}px text-spacing   ${x}`));
  await ev(`(function(){var s=document.getElementById('ts');if(s)s.remove();})()`); await sleep(200);
}
ws.close(); proc.kill(); srv.close();

console.log(`layout check — ${WIDTHS.length} widths, plus text-spacing at ${SPACING_WIDTHS.join(' and ')}`);
if (bad.length) { console.log(`\n${bad.length} VIOLATION(S):`); bad.forEach(v => console.log('  ' + v)); process.exit(1); }
console.log('all layout laws hold.');
process.exit(0);
