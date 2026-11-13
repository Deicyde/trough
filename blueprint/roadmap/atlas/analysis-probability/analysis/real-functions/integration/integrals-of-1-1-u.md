---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry14Qreflection.ramanujan_part1_ch8_entry14_qreflection, MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry14VIntegral5.ramanujan_part1_ch8_entry14_v_integral5, MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry14ViIntegral6.ramanujan_part1_ch8_entry14_vi_integral6, MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry14ViiIntegral8.ramanujan_part1_ch8_entry14_vii_integral8
statement: formalized
proof: formalized
---

# Integrals of 1/(1 + uⁿ)

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/integrals-of-1-1-u/index.html).

## Ramanujan's closed form for $\int_0^x du/(1 + u^{10})$ (Chapter 8, Entry 14)

Put
$a_\pm = \sqrt{6 \pm 2\sqrt5}$ and $b_\pm = \sqrt{10 \pm 2\sqrt5}$. For every real $x$ with
$0 \le x < 1$,

$$\int_0^x \frac{du}{1 + u^{10}} = \frac{\arctan x}{5} +
\frac{a_+}{20} \arctan \frac{a_+ x}{2(1 - x^2)} + \frac{a_-}{20} \arctan \frac{a_- x}{2(1 - x^2)} +
\frac{b_+}{40} \log \frac{1 + b_+ x/2 + x^2}{1 - b_+ x/2 + x^2} +
\frac{b_-}{40} \log \frac{1 + b_- x/2 + x^2}{1 - b_- x/2 + x^2}.$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 8.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry14Qreflection.ramanujan_part1_ch8_entry14_qreflection`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry14Qreflection.lean, line 417](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry14Qreflection.lean#L417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/integrals-of-1-1-u/index.html#ramanujan-part1-ch8-entry14-qreflection).

## Ramanujan's closed form for $\int_0^x du/(1 + u^5)$ (Chapter 8, Entry 14(v))

Let $x$ be
a real number with $-1 < x < 4/(\sqrt5 + 1)$, and put $c_\pm = \sqrt{10 \pm 2\sqrt5}$ and

$$Q(x) = \frac{1 + \tfrac12 x(\sqrt5 - 1) + x^2}{1 - \tfrac12 x(\sqrt5 + 1) + x^2}.$$

Then $u \mapsto 1/(1 + u^5)$ is integrable on the interval between $0$ and $x$,
$(1 + x)^5/(1 + x^5) > 0$, $Q(x) > 0$, $4 + x(\sqrt5 - 1) \ne 0$, $4 - x(\sqrt5 + 1) \ne 0$, and

$$\int_0^x \frac{du}{1 + u^5} = \frac{1}{20} \log \frac{(1 + x)^5}{1 + x^5} +
\frac{1}{4\sqrt5} \log Q(x) + \frac{c_+}{10} \arctan \frac{c_+ x}{4 + x(\sqrt5 - 1)} +
\frac{c_-}{10} \arctan \frac{c_- x}{4 - x(\sqrt5 + 1)}.$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 8, Entry 14(v), pp. 189–191.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry14VIntegral5.ramanujan_part1_ch8_entry14_v_integral5`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry14VIntegral5.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry14VIntegral5.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/integrals-of-1-1-u/index.html#ramanujan-part1-ch8-entry14-v-integral5).

## Ramanujan's closed form for $\int_0^x du/(1 + u^6)$ (Chapter 8, Entry 14(vi))

For every
real number $x$, the function $u \mapsto 1/(1 + u^6)$ is integrable on the interval between $0$
and $x$, $1 + \sqrt3\,x + x^2 > 0$, $1 - \sqrt3\,x + x^2 > 0$, and

$$\int_0^x \frac{du}{1 + u^6} = \frac12 \arctan x + \frac16 \arctan x^3 +
\frac{1}{4\sqrt3} \log \frac{1 + \sqrt3\,x + x^2}{1 - \sqrt3\,x + x^2}.$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 8, Entry 14(vi), pp. 189–190.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry14ViIntegral6.ramanujan_part1_ch8_entry14_vi_integral6`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry14ViIntegral6.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry14ViIntegral6.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/integrals-of-1-1-u/index.html#ramanujan-part1-ch8-entry14-vi-integral6).

## Ramanujan's closed form for $\int_0^x du/(1 + u^8)$ (Chapter 8, Entry 14(vii))

Put
$s_\pm = \sqrt{2 \pm \sqrt2}$ and, for real $x$,
$R_\pm(x) = \frac{1 + s_\pm x + x^2}{1 - s_\pm x + x^2}$. For every real $x$ with $|x| < 1$, the
function $u \mapsto 1/(1 + u^8)$ is integrable on the interval between $0$ and $x$, $R_+(x) > 0$,
$R_-(x) > 0$, $1 - x^2 \ne 0$, and

$$\int_0^x \frac{du}{1 + u^8} = \frac{s_+}{16} \left( \log R_+(x) +
2 \arctan \frac{s_+ x}{1 - x^2} \right) + \frac{s_-}{16} \left( \log R_-(x) +
2 \arctan \frac{s_- x}{1 - x^2} \right).$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 8, Entry 14(vii), pp. 189–190.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry14ViiIntegral8.ramanujan_part1_ch8_entry14_vii_integral8`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry14ViiIntegral8.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry14ViiIntegral8.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/integrals-of-1-1-u/index.html#ramanujan-part1-ch8-entry14-vii-integral).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integrals of 1/(1 + uⁿ)](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/integrals-of-1-1-u/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/real-functions/integration/integrals-of-1-1-u)
