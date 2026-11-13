---
declaration: section
origin: cited
lean: MetaMathlibExt.modifiedBesselI_term, MetaMathlibExt.modifiedBesselI, MetaMathlibExt.modifiedBesselI_zero, MetaMathlibExt.modifiedBesselI_one
statement: formalized
proof: formalized
---

# Modified Bessel functions of the first kind

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/modified-bessel-functions-of-the-first-kind/index.html).

## Terms of the modified Bessel series

For natural numbers $m, k$ and a real number $x$, the
$k$-th term of the series for the modified Bessel function of the first kind of order $m$ is
$x^{2k+m} / (2^{2k+m} \, k! \, (k+m)!)$.

Formalized by `MetaMathlibExt.modifiedBesselI_term`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/ModifiedBesselFirstKind.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ModifiedBesselFirstKind.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/modified-bessel-functions-of-the-first-kind/index.html#modified-bessel-i-term).

## Modified Bessel function of the first kind

For a natural number $m$ and real $x$, the
modified Bessel function of the first kind of order $m$ is
$I_m(x) = \sum_{k \ge 0} x^{2k+m} / (2^{2k+m} \, k! \, (k+m)!)$.

Formalized by `MetaMathlibExt.modifiedBesselI`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/ModifiedBesselFirstKind.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ModifiedBesselFirstKind.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/modified-bessel-functions-of-the-first-kind/index.html#modified-bessel-i).

## Modified Bessel function of the first kind of order zero

For a real number $x$, $I_0(x)$
is the modified Bessel function of the first kind of order $0$ at $x$, that is,
$I_0(x) = \sum_{k \ge 0} x^{2k} / (2^{2k} \, (k!)^2)$.

Formalized by `MetaMathlibExt.modifiedBesselI_zero`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/ModifiedBesselFirstKind.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ModifiedBesselFirstKind.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/modified-bessel-functions-of-the-first-kind/index.html#modified-bessel-i-zero).

## Modified Bessel function of the first kind of order one

For a real number $x$, $I_1(x)$
is the modified Bessel function of the first kind of order $1$ at $x$, that is,
$I_1(x) = \sum_{k \ge 0} x^{2k+1} / (2^{2k+1} \, k! \, (k+1)!)$.

Formalized by `MetaMathlibExt.modifiedBesselI_one`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/ModifiedBesselFirstKind.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ModifiedBesselFirstKind.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/modified-bessel-functions-of-the-first-kind/index.html#modified-bessel-i-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Modified Bessel functions of the first kind](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/modified-bessel-functions-of-the-first-kind/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/special-functions/elementary-transcendental-functions/modified-bessel-functions-of-the-first-kind)
