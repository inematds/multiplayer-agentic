// Confere as páginas de guia/: rolagem horizontal (360–1920 px), imagens quebradas e links internos.
// Uso: NODE_PATH=~/.npm-global/lib/node_modules node tools/checar.cjs [pt|en|es ...]
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const raiz = path.resolve(__dirname, '..', 'guia');
  const langs = process.argv.slice(2).length ? process.argv.slice(2) : ['pt', 'en', 'es'];
  const browser = await chromium.launch();
  let erros = 0;
  for (const lang of langs) {
    const dir = lang === 'pt' ? raiz : path.join(raiz, lang);
    if (!fs.existsSync(dir)) { console.log(`[${lang}] sem pasta`); continue; }
    const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));
    for (const w of [360, 800, 1280, 1920]) {
      const page = await browser.newPage({ viewport: { width: w, height: 900 } });
      for (const f of files) {
        await page.goto('file://' + path.join(dir, f));
        await page.waitForLoadState('load');
        const r = await page.evaluate(() => ({
          over: document.documentElement.scrollWidth - innerWidth,
          imgs: [...document.images].filter(i => i.complete && i.naturalWidth === 0).map(i => i.getAttribute('src')),
          links: [...document.querySelectorAll('a[href]')].map(a => a.getAttribute('href'))
            .filter(h => !/^(https?:|#|mailto:)/.test(h)),
        }));
        if (r.over > 1) { console.log(`[${lang}] ${f} @${w}: rolagem horizontal ${r.over}px`); erros++; }
        if (w === 1280) {
          if (r.imgs.length) { console.log(`[${lang}] ${f}: imagem quebrada ${r.imgs}`); erros++; }
          for (const h of r.links) {
            const alvo = path.resolve(dir, h.split('#')[0] || f);
            const ok = fs.existsSync(alvo) && (fs.statSync(alvo).isFile() || fs.existsSync(path.join(alvo, 'index.html')));
            if (!ok) { console.log(`[${lang}] ${f}: link quebrado ${h}`); erros++; }
          }
        }
      }
      await page.close();
    }
    console.log(`[${lang}] ${files.length} páginas conferidas`);
  }
  await browser.close();
  console.log(erros ? `FALHOU: ${erros} problema(s)` : 'OK: nenhum problema');
  process.exit(erros ? 1 : 0);
})();
