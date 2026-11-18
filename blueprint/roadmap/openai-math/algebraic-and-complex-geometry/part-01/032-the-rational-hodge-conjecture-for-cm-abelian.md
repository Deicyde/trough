---
declaration: section
origin: cited
lean: HodgeCM.hodge_conjecture_for_cm_abelian_varieties
statement: formalized
proof: formalized
---

# 032. The rational Hodge conjecture for CM abelian varieties

5 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the rational Hodge conjecture for every complex CM abelian variety, in every dimension and codimension. Through Milne's theorems, this also gives the Tate conjecture for all abelian varieties over finite fields and the Hodge standard conjecture for abelian varieties in every characteristic.

## The rational Hodge conjecture for CM abelian varieties

We prove the rational Hodge conjecture for complex abelian varieties with complex multiplication: every rational Hodge class on such a variety is a rational linear combination of algebraic cycle classes. As consequences, we obtain the generalized Hodge conjecture for CM abelian varieties, the Tate conjecture for abelian varieties over finite fields, and the Hodge standard conjecture for abelian varieties in arbitrary characteristic.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/paper.pdf); the Lean below formalizes results from it.

## Algebraic Kuga–Satake correspondences and Hodge conjectures on a K3 quadratic locus

We prove the rational Hodge and generalized Hodge conjectures in every cohomological degree of every self-power of a projective complex K3 surface whose transcendental quadratic space, with its cup-product form, admits a rational isometric embedding in $\mathbb U_{\mathbb Q}^{\oplus2}\perp\langle-1\rangle^4$. This includes every ample *P*-polarized K3 surface, including all Picard jumps, for $P=\mathbb U\oplus D_8(-1)\oplus D_4(-1)$. On this locus we construct algebraic correspondences inducing every prescribed standard even-Clifford Kuga–Satake tensor. More generally, for any projective complex K3 surface, algebraicity of one exact standard even-Clifford Kuga–Satake tensor implies both conjectures for every self-power.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Algebraic-Kuga-Satake-correspondences-and-Hodge-conjectures-on-a-K3-quadratic-locus-September-30-2026/paper.pdf).

## Weil classes and Hodge classes on abelian powers

We prove the rational Hodge conjecture in every codimension on every self-power of a complex abelian sixfold with an imaginary-quadratic action and a compatible polarization whose rational homological Hermitian form is hyperbolic of signature $(3,3)$. We also prove it in every codimension on every self-power of a complex abelian variety of dimension at most five admitting an imaginary-quadratic action. Both results include nonsimple varieties and special periods with additional endomorphisms. The proof uses the companion theorem on the rational Hodge conjecture for CM abelian varieties.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026/paper.pdf).

## Abelian covers, Gale correspondences, and the Hodge conjecture for powers

We prove the rational Hodge conjecture on every self-power of the Jacobian at each tensor Hodge-generic point of the full marked variation of a connected abelian cover of curves. This holds in every base genus and for every compatible branching pattern. For any CM abelian variety, the conclusion also holds for every self-power of its product with the Jacobian, on the same Hodge-generic locus. We also prove the conjecture on every self-power of a very general member of the full smooth labelled family of diagonal complete intersections cut out by at most two equations of a common degree, in every dimension and every degree at least two.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026/paper.pdf).

## A Conditional Reduction for Algebraic Kuga–Satake Correspondences

For a polarized K3 surface whose primitive cohomology has full orthogonal Hodge group, one algebraic correspondence inducing a nonzero map from that cohomology to the second cohomology of an abelian variety suffices to recover the prescribed full Kuga–Satake correspondence. We give an equivalent condition using holomorphic one-forms on a generically finite surface cover. If this input holds very generally in a polarized component, the prescribed correspondence is algebraic throughout that component, for every choice of standard data on the transcendental part. The existence of the initial correspondence remains a hypothesis.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Conditional-Reduction-for-Algebraic-Kuga-Satake-Correspondences-September-10-2026/paper.pdf).

## The Lean formalization

The formalization proves that every rational Hodge class on a complex CM abelian variety is algebraic. For a smooth integral projective group scheme $X$ over $\mathbb C$ with the stated complex-multiplication data and every $p\ge0$, each rational Hodge class of degree $2p$ is a rational linear combination of cycle classes of codimension-$p$ algebraic subvarieties. The result applies in every dimension and codimension.

The complex-multiplication hypothesis is expressed on geometric rational $H^1$: it is a finite direct sum of rank-one vector spaces over CM number fields, and their diagonal action preserves the holomorphic Hodge filtration under the rational-to-de Rham comparison. The fields may differ among the summands.

The paper's consequences for the Tate conjecture over finite fields and the Hodge standard conjecture in arbitrary characteristic are outside this selected statement.

We thank the contributors to [HodgeConjecture](https://github.com/Paul-Lez/HodgeConjecture) (which itself adapts [sphere-six-complex](https://github.com/deancureton/sphere-six-complex) and [mathlib4](https://github.com/leanprover-community/mathlib4)) for their Lean statement of the Hodge conjecture, which was used for the Comparator challenge.

## Lean: Rational Hodge classes on CM abelian varieties are algebraic

```lean
theorem hodge_conjecture_for_cm_abelian_varieties
    (X : Over (Spec ↧ℂ)) [IsIntegral X.left] [Smooth X.hom]
    [_root_.OAI.AlgebraicGeometry.Foundations.ProjectiveSpaceIs.IsProjective X.hom] [GrpObj X]
    (hCM : _root_.OAI.AlgebraicGeometry.ComplexMultiplication.Definitions.HasComplexMultiplication X) (p : ℕ) :
    Hdg^p(X; ℚ) ≤ _root_.OAI.AlgebraicGeometry.ComplexPoint.Basic.ComplexSchemePoint.algebraicCycleClassSpan X p
```

Stated in [Challenge.lean, line 38](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HodgeConjectureCMAbelianVarieties/Challenge.lean#L38). Proved in [lean/ComparatorChallenges/HodgeConjectureCMAbelianVarieties/Solution.lean, line 11](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HodgeConjectureCMAbelianVarieties/Solution.lean#L11). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/032.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/032.md)
