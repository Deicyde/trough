---
declaration: section
origin: cited
lean: Real.log_sub_log_floor_le, Real.abs_harmonic_sub_log_sub_eulerMascheroniConstant_le, Real.abs_harmonic_floor_sub_log_sub_eulerMascheroniConstant_le, Real.isBigO_harmonic_floor_sub_log_sub_eulerMascheroniConstant
statement: formalized
proof: formalized
---

# Harmonic numbers and the Euler–Mascheroni constant

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/harmonic-numbers-and-the-euler-mascheroni-consta/index.html).

## Logarithm gap between a real number and its floor

For every real $x \ge 1$, the floor
$\lfloor x \rfloor$ of $x$ satisfies $\log x - \log \lfloor x \rfloor \le 1/\lfloor x \rfloor$.

Formalized by `Real.log_sub_log_floor_le`, a theorem declared in [MathlibExt/NumberTheory/Harmonic/EulerMascheroniBounds.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Harmonic/EulerMascheroniBounds.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/harmonic-numbers-and-the-euler-mascheroni-consta/index.html#log-sub-log-floor-le).

## Explicit harmonic error bound at integers

Let $H_n = \sum_{k=1}^{n} 1/k$ be the $n$-th
harmonic number and $\gamma$ the Euler–Mascheroni constant. For every natural number $n \ge 1$,
$|H_n - \log n - \gamma| \le 1/n$.

Formalized by `Real.abs_harmonic_sub_log_sub_eulerMascheroniConstant_le`, a theorem declared in [MathlibExt/NumberTheory/Harmonic/EulerMascheroniBounds.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Harmonic/EulerMascheroniBounds.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/harmonic-numbers-and-the-euler-mascheroni-consta/index.html#abs-harmonic-sub-log-sub-euler-mascheron).

## Explicit harmonic error bound at real arguments

Let $H_n = \sum_{k=1}^{n} 1/k$ be the
$n$-th harmonic number and $\gamma$ the Euler–Mascheroni constant. For every real $x \ge 2$,
with $\lfloor x \rfloor$ the floor of $x$, $|H_{\lfloor x \rfloor} - \log x - \gamma| \le 2/x$.

Formalized by `Real.abs_harmonic_floor_sub_log_sub_eulerMascheroniConstant_le`, a theorem declared in [MathlibExt/NumberTheory/Harmonic/EulerMascheroniBounds.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Harmonic/EulerMascheroniBounds.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/harmonic-numbers-and-the-euler-mascheroni-consta/index.html#abs-harmonic-floor-sub-log-sub-euler-mas).

## Harmonic numbers at the floor track the logarithm

Let $H_k$ denote the $k$-th harmonic
number, $\lfloor x \rfloor$ the floor of a real number $x$, and $\gamma$ the Euler–Mascheroni
constant. Then $H_{\lfloor x \rfloor} - \log x - \gamma = O(1/x)$ as $x \to \infty$.

Formalized by `Real.isBigO_harmonic_floor_sub_log_sub_eulerMascheroniConstant`, a theorem declared in [MathlibExt/NumberTheory/Harmonic/Floor.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Harmonic/Floor.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/harmonic-numbers-and-the-euler-mascheroni-consta/index.html#is-big-o-harmonic-floor-sub-log-sub-eule).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Harmonic numbers and the Euler–Mascheroni constant](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/harmonic-numbers-and-the-euler-mascheroni-consta/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/special-numbers/harmonic-numbers/harmonic-numbers-and-the-euler-mascheroni-consta)
