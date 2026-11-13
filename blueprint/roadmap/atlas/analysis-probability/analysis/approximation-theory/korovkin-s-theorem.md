---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.Korovkin.korovkinId, MathlibExt.Analysis.FunctionalAnalysis.Korovkin.korovkinIdSq, MathlibExt.Analysis.FunctionalAnalysis.Korovkin.korovkinShiftSq, MathlibExt.Analysis.FunctionalAnalysis.Korovkin.korovkinShiftSq_eq, MathlibExt.Analysis.FunctionalAnalysis.Korovkin.tendsto_apply_of_tendsto, MathlibExt.Analysis.FunctionalAnalysis.Korovkin.le_apply_of_le, MathlibExt.Analysis.FunctionalAnalysis.Korovkin.abs_apply_le, MathlibExt.Analysis.FunctionalAnalysis.Korovkin.abs_sub_le_add_sq
statement: formalized
proof: formalized
---

# Korovkin's theorem

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/korovkin-s-theorem/index.html).

## The identity test function

The function $x \mapsto x$ on $[0, 1]$, as an element
of $C([0, 1], \mathbb{R})$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.Korovkin.korovkinId`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/Korovkin.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/Korovkin.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/korovkin-s-theorem/index.html#korovkin-id).

## The square test function

The function $x \mapsto x^2$ on $[0, 1]$, as an element
of $C([0, 1], \mathbb{R})$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.Korovkin.korovkinIdSq`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/Korovkin.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/Korovkin.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/korovkin-s-theorem/index.html#korovkin-id-sq).

## The shifted square

For $x \in [0, 1]$, the function $y \mapsto (y - x)^2$
on $[0, 1]$, as an element of $C([0, 1], \mathbb{R})$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.Korovkin.korovkinShiftSq`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/Korovkin.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/Korovkin.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/korovkin-s-theorem/index.html#korovkin-shift-sq).

## Expansion of the shifted square

Write $e(y) = y$ and $q(y) = y^2$ for the identity
and square functions and $1$ for the constant function one, as elements of
$C([0, 1], \mathbb{R})$. For every $x \in [0, 1]$, the function $y \mapsto (y - x)^2$ in
$C([0, 1], \mathbb{R})$ equals $q - 2x \cdot e + x^2 \cdot 1$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.Korovkin.korovkinShiftSq_eq`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/Korovkin.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/Korovkin.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/korovkin-s-theorem/index.html#korovkin-shift-sq-eq).

## Uniform convergence implies pointwise convergence

If a sequence $(u_n)$ in
$C([0, 1], \mathbb{R})$ converges to $e$ in the sup norm, then $u_n(x) \to e(x)$ for every
$x \in [0, 1]$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.Korovkin.tendsto_apply_of_tendsto`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/Korovkin.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/Korovkin.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/korovkin-s-theorem/index.html#tendsto-apply-of-tendsto).

## Positive linear operators are monotone

Let $L$ be a real-linear operator on
$C([0, 1], \mathbb{R})$ that is positive: $(L f)(x) \ge 0$ for all $x \in [0, 1]$ whenever
$f(x) \ge 0$ for all $x \in [0, 1]$. If $g, h \in C([0, 1], \mathbb{R})$ satisfy
$g(x) \le h(x)$ for all $x \in [0, 1]$, then $(L g)(x) \le (L h)(x)$
for every $x \in [0, 1]$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.Korovkin.le_apply_of_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/Korovkin.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/Korovkin.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/korovkin-s-theorem/index.html#le-apply-of-le).

## Positive linear operators bound absolute values

Let $L$ be a real-linear
operator on $C([0, 1], \mathbb{R})$ that is positive: $(L f)(x) \ge 0$ for all
$x \in [0, 1]$ whenever $f(x) \ge 0$ for all $x \in [0, 1]$. If
$g, h \in C([0, 1], \mathbb{R})$ satisfy $|g(y)| \le h(y)$ for all $y \in [0, 1]$, then
$|(L g)(x)| \le (L h)(x)$ for every $x \in [0, 1]$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.Korovkin.abs_apply_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/Korovkin.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/Korovkin.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/korovkin-s-theorem/index.html#abs-apply-le).

## Quadratic bound from a modulus of continuity

Let $f \in C([0, 1], \mathbb{R})$
have sup norm $\|f\|$, let $x \in [0, 1]$, and let $\delta > 0$, $\varepsilon \ge 0$
and $C \ge 0$ be real numbers with $2\|f\| \le C \delta^2$. If
$|f(y) - f(x)| < \varepsilon$ for every $y \in [0, 1]$ with $|y - x| < \delta$, then
$|f(y) - f(x)| \le \varepsilon + C (y - x)^2$ for every $y \in [0, 1]$.

Korovkin's theorem applies this with $C = 2\|f\| / \delta^2$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.Korovkin.abs_sub_le_add_sq`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/Korovkin.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/Korovkin.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/korovkin-s-theorem/index.html#abs-sub-le-add-sq).

## Korovkin's theorem

Write $e_0$, $e_1$ and $e_2$ for the functions $x \mapsto 1$,
$x \mapsto x$ and $x \mapsto x^2$ in $C([0, 1], \mathbb{R})$.
Let $(L_n)_{n \in \mathbb{N}}$ be real-linear operators on $C([0, 1], \mathbb{R})$, each
positive: $(L_n f)(x) \ge 0$ for all $x \in [0, 1]$ whenever $f(x) \ge 0$ for all
$x \in [0, 1]$. If $L_n e_i \to e_i$ in the sup norm for $i = 0, 1, 2$, then
$L_n f \to f$ in the sup norm for every $f \in C([0, 1], \mathbb{R})$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.Korovkin.korovkin`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/Korovkin.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/Korovkin.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/korovkin-s-theorem/index.html#korovkin).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Korovkin's theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/korovkin-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/approximation-theory/korovkin-s-theorem)
