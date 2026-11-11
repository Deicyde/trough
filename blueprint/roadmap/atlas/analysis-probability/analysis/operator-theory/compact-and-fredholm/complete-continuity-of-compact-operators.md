---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Normed.Operator.CompleteContinuity.tendsto_apply_of_isCompactOperator_of_forall_tendsto, MathlibExt.Analysis.Normed.Operator.CompleteContinuity.tendsto_apply_of_isCompactOperator_of_tendsto_zero, MathlibExt.Analysis.Normed.Operator.CompleteContinuity.tendsto_apply_of_isCompactOperator_of_tendsto_weakSpace
statement: formalized
proof: formalized
---

# Complete continuity of compact operators

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/complete-continuity-of-compact-operators/index.html).

## Complete continuity of compact operators

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $E$ and $F$ be normed spaces over $\mathbb{K}$, and let $T : E \to F$ be a
compact continuous linear operator. If a sequence $(u_n)$ in $E$ converges weakly to $x \in E$,
that is, $f(u_n) \to f(x)$ for every continuous linear functional $f : E \to \mathbb{K}$, then
$T u_n \to T x$ in norm.

The proof is the standard subsequence argument: if $T u_n$ did not converge in norm to $T x$,
some subsequence would stay $\varepsilon$-away from $T x$; the sequence $(u_n)$ is norm-bounded
by uniform boundedness, so compactness gives a further subsequence of $(T u_n)$ converging in
norm to some $a$; but $T$ preserves weak convergence, so $a = T x$ by uniqueness of scalar
limits and the fact that the dual separates points, contradicting the
$\varepsilon$-separation.

Formalized by `MathlibExt.Analysis.Normed.Operator.CompleteContinuity.tendsto_apply_of_isCompactOperator_of_forall_tendsto`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/CompleteContinuity.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Operator/CompleteContinuity.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/complete-continuity-of-compact-operators/index.html#tendsto-apply-of-is-compact-operator-of).

## Compact operators send weakly null sequences to norm null sequences

Let $\mathbb{K}$
be $\mathbb{R}$ or $\mathbb{C}$, let $E$ and $F$ be normed spaces over $\mathbb{K}$, and let
$T : E \to F$ be a compact continuous linear operator. If a sequence $(u_n)$ in $E$ converges
weakly to $0$, that is, $f(u_n) \to 0$ for every continuous linear functional
$f : E \to \mathbb{K}$, then $T u_n \to 0$ in norm.

Formalized by `MathlibExt.Analysis.Normed.Operator.CompleteContinuity.tendsto_apply_of_isCompactOperator_of_tendsto_zero`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/CompleteContinuity.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Operator/CompleteContinuity.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/complete-continuity-of-compact-operators/index.html#tendsto-apply-of-is-compact-operator-of-2).

## Complete continuity of compact operators, weak-topology form

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $E$ and $F$ be normed spaces over $\mathbb{K}$, and let
$T : E \to F$ be a compact continuous linear operator. If a sequence $(u_n)$ in $E$ converges
to $x \in E$ in the weak topology of $E$, then $T u_n \to T x$ in norm.

Formalized by `MathlibExt.Analysis.Normed.Operator.CompleteContinuity.tendsto_apply_of_isCompactOperator_of_tendsto_weakSpace`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/CompleteContinuity.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Operator/CompleteContinuity.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/complete-continuity-of-compact-operators/index.html#tendsto-apply-of-is-compact-operator-of-3).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Complete continuity of compact operators](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/complete-continuity-of-compact-operators/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/compact-and-fredholm/complete-continuity-of-compact-operators)
