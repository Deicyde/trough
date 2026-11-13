---
declaration: section
origin: cited
lean: MathlibExt.Dynamics.KAMWanted.Dynamics.IsDiophantine, MathlibExt.Dynamics.KAMWanted.Dynamics.kam_invariant_curve
statement: formalized
---

# Kolmogorov–Arnold–Moser theorem

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/kolmogorov-arnold-moser-theorem/index.html).

## Diophantine number

A real number $\alpha$ is Diophantine (with exponent $2$, as used in
KAM theory) if there is $C > 0$ such that $C / q^2 \le |\alpha - p/q|$ for all integers $p$ and
$q$ with $q \neq 0$.

Formalized by `MathlibExt.Dynamics.KAMWanted.Dynamics.IsDiophantine`, a definition declared in [WantedExt/Dynamics/KAMWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/KAMWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/kolmogorov-arnold-moser-theorem/index.html#is-diophantine).

## KAM theorem for twist maps (persistence of an invariant curve)

Let $\alpha$ be a
Diophantine real number and let $f : \mathbb{R} \to \mathbb{R}$ be real-analytic, $1$-periodic and
not constant, with $\int_0^1 f(x)\,dx = 0$. Then there is $c_0 > 0$ such that for every real $c$
with $|c| < c_0$ there is a $C^\infty$, strictly increasing function $q : \mathbb{R} \to \mathbb{R}$
such that $t \mapsto q(t) - t$ is $1$-periodic and, for every real $t$,

$$q(t + \alpha) - 2q(t) + q(t - \alpha) = c\, f(q(t)).$$

## Sources

- A. N. Kolmogorov (1954); V. I. Arnold (1963); J. Moser, *On invariant curves of area-preserving mappings of an annulus*, Nachr. Akad. Wiss. Göttingen (1962). Knill, *Some fundamental theorems in mathematics*, §83. Problem `kam_invariant_curve` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Dynamics.KAMWanted.Dynamics.kam_invariant_curve` is written with `theorem_wanted` in [WantedExt/Dynamics/KAMWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/KAMWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/kolmogorov-arnold-moser-theorem/index.html#kam-invariant-curve).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kolmogorov–Arnold–Moser theorem](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/kolmogorov-arnold-moser-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Dynamics/smooth-dynamics/kolmogorov-arnold-moser-theorem)
