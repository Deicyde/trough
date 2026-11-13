---
declaration: section
origin: cited
lean: MetaMathlibExt.IsBangZsigmondyExceptional, MetaMathlibExt.bangZsigmondy_exists_primitivePrimeDivisor
statement: formalized
proof: formalized
---

# Zsigmondy's theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/zsigmondy-s-theorem/index.html).

## Exceptional cases of Zsigmondy's theorem

A triple $(a, b, n)$ of natural numbers is a
Bang–Zsigmondy exceptional case when either $(a, b, n) = (2, 1, 6)$, or $n = 2$ and $a + b = 2^k$
for some natural number $k$.

Formalized by `MetaMathlibExt.IsBangZsigmondyExceptional`, a definition declared in [MathlibExt/NumberTheory/BangZsigmondy.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/BangZsigmondy.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/zsigmondy-s-theorem/index.html#is-bang-zsigmondy-exceptional).

## Zsigmondy's theorem

Let $a$, $b$ and $n$ be natural numbers with $0 < b < a$, $a$ and $b$
coprime, and $n \ge 2$, and suppose that $(a, b, n)$ is not a Bang–Zsigmondy exceptional case:
neither $(a, b, n) = (2, 1, 6)$, nor $n = 2$ with $a + b$ a power of two. Then $a^n - b^n$ has a
primitive prime divisor, that is, a prime $p$ that divides $a^n - b^n$ and divides no $a^m - b^m$
with $1 \le m < n$.

## Sources

- Bayarmagnai lines 133–137 invoke the general theorem, with the explicit exception families per Jones Theorem `Bang` lines 211–215.

Formalized by `MetaMathlibExt.bangZsigmondy_exists_primitivePrimeDivisor`, a theorem declared in [MathlibExt/NumberTheory/BangZsigmondy.lean, line 1203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/BangZsigmondy.lean#L1203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/zsigmondy-s-theorem/index.html#bang-zsigmondy-exists-primitive-prime-di).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Zsigmondy's theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/zsigmondy-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/zsigmondy-s-theorem)
