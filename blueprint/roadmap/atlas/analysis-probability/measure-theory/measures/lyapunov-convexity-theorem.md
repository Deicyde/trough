---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.Integral.LyapunovConvexityWanted.lyapunovRange, MathlibExt.MeasureTheory.Integral.LyapunovConvexityWanted.lyapunov_convexity
statement: formalized
proof: formalized
---

# Lyapunov convexity theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/lyapunov-convexity-theorem/index.html).

## Lyapunov range

For a measure $\mu$ on a measurable space $\alpha$ and a function
$f : \alpha \to E$ into a real normed space $E$, the Lyapunov range of $f$ with respect to $\mu$ is
the set $\lbrace \int_s f \, d\mu : s \subseteq \alpha \text{ measurable} \rbrace$ of integrals of
$f$ over measurable subsets of $\alpha$.

Here $\int_s f \, d\mu$ is the Bochner integral, which is $0$ when $f$ is not integrable on $s$
or when $E$ is not complete.

Formalized by `MathlibExt.MeasureTheory.Integral.LyapunovConvexityWanted.lyapunovRange`, a definition declared in [MathlibExt/MeasureTheory/Integral/LyapunovConvexity.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Integral/LyapunovConvexity.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/lyapunov-convexity-theorem/index.html#lyapunov-range).

## Lyapunov convexity theorem

Let $\mu$ be a finite atomless measure on a measurable space
$\alpha$, let $E$ be a finite-dimensional real normed space, and let $f : \alpha \to E$ be Bochner
integrable with respect to $\mu$. Then the Lyapunov range of $f$ with respect to $\mu$, the set of
integrals $\int_s f \, d\mu$ over measurable sets $s \subseteq \alpha$, is compact and convex.

## Sources

- A. Lyapunov, Izv. Akad. Nauk SSSR 4 (1940) 465–478; Diestel-Uhl, Vector Measures; Lean states atomless finite measure case with Bochner integrable finite-dim integrand, infinite-dim fails.

Formalized by `MathlibExt.MeasureTheory.Integral.LyapunovConvexityWanted.lyapunov_convexity`, a theorem declared in [MathlibExt/MeasureTheory/Integral/LyapunovConvexity.lean, line 1802](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Integral/LyapunovConvexity.lean#L1802). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/lyapunov-convexity-theorem/index.html#lyapunov-convexity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lyapunov convexity theorem](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/lyapunov-convexity-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/measures/lyapunov-convexity-theorem)
