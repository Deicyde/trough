---
declaration: module
origin: cited
lean: Matrix.exp_add_mem_of_isClosed, Matrix.lieAlgebraOfIsClosed, Matrix.mem_lieAlgebraOfIsClosed_iff, Matrix.conj_mem_lieAlgebraOfIsClosed, Matrix.commutator_mem_lieAlgebraOfIsClosed
statement: formalized
proof: formalized
---

# The Lie algebra of a closed group of matrices

The module `PhyslibAlpha.Mathematics.ForMathlib.Analysis.Normed.Algebra.MatrixLieAlgebra`, [PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/MatrixLieAlgebra.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/MatrixLieAlgebra.lean): 5 declarations, 4 with a docstring.

> The generators of the one-parameter subgroups of a closed subgroup of `GL(κ, ℂ)`.

## i. Overview

> For a subgroup `H` of `GL(κ, ℂ)`, the generators of its one-parameter subgroups are the
> matrices `X` with `exp (t X) ∈ H` for every real `t`. When `H` is closed they form a real
> subspace `lieAlgebraOfIsClosed H hH`, its Lie algebra:
>
> * closure under real multiples is immediate;
> * closure under addition is the Lie product formula: `exp (t (X + Y))` is the limit of
>   `(exp (t X / n) exp (t Y / n)) ^ n`, a sequence in `H` whose inverses also converge, so the
>   limit lies in `H` because `H` is closed.
>
> The Lie algebra is invariant under conjugation by `H`, and it is closed under the
> commutator: it is a closed subspace containing the conjugates `exp (t X) Y exp (−t X)`, and
> so their derivative `X Y − Y X` at `t = 0`.

## ii. Key results

> - `Matrix.exp_add_mem_of_isClosed` : the one-parameter subgroups of a closed group of
>   matrices are closed under adding generators.
> - `Matrix.lieAlgebraOfIsClosed` : the Lie algebra of a closed group of matrices.
> - `Matrix.conj_mem_lieAlgebraOfIsClosed` : it is invariant under conjugation by the group.
> - `Matrix.commutator_mem_lieAlgebraOfIsClosed` : it is closed under the commutator.

## iv. References

> * B. C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer (2015).

## A. Closure under addition

**`Matrix.exp_add_mem_of_isClosed`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/MatrixLieAlgebra.lean#L70).

> In a closed group of matrices, if the one-parameter subgroups of `X` and of `Y` lie in
> the group, then so does `exp (X + Y)`: it is the limit of the products
> `(exp (X / n) exp (Y / n)) ^ n` of group elements, by the Lie product formula.

```lean
lemma exp_add_mem_of_isClosed {H : Subgroup (GeneralLinearGroup κ ℂ)}
    (hH : IsClosed (H : Set (GeneralLinearGroup κ ℂ))) {X Y : Matrix κ κ ℂ}
    (hX : ∀ t : ℝ, exp (t • X) ∈ Set.range fun g : H => (g.1 : Matrix κ κ ℂ))
    (hY : ∀ t : ℝ, exp (t • Y) ∈ Set.range fun g : H => (g.1 : Matrix κ κ ℂ)) :
    exp (X + Y) ∈ Set.range fun g : H => (g.1 : Matrix κ κ ℂ)
```

## B. The Lie algebra

**`Matrix.lieAlgebraOfIsClosed`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/MatrixLieAlgebra.lean#L117).

> The Lie algebra of a closed subgroup of `GL(κ, ℂ)`: the real subspace of matrices whose
> one-parameter subgroups lie in the group.

```lean
def lieAlgebraOfIsClosed (H : Subgroup (GeneralLinearGroup κ ℂ))
    (hH : IsClosed (H : Set (GeneralLinearGroup κ ℂ))) : Submodule ℝ (Matrix κ κ ℂ)
```

**`Matrix.mem_lieAlgebraOfIsClosed_iff`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/MatrixLieAlgebra.lean#L132).

```lean
lemma mem_lieAlgebraOfIsClosed_iff {H : Subgroup (GeneralLinearGroup κ ℂ)}
    {hH : IsClosed (H : Set (GeneralLinearGroup κ ℂ))} {X : Matrix κ κ ℂ} :
    X ∈ lieAlgebraOfIsClosed H hH ↔
      ∀ t : ℝ, exp (t • X) ∈ Set.range fun g : H => (g.1 : Matrix κ κ ℂ)
```

## C. Conjugation and the commutator

**`Matrix.conj_mem_lieAlgebraOfIsClosed`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/MatrixLieAlgebra.lean#L148).

> The Lie algebra is invariant under conjugation by the group: the one-parameter subgroup
> of the conjugate of a generator by a group element is the conjugate of the one-parameter
> subgroup of the generator.

```lean
lemma conj_mem_lieAlgebraOfIsClosed (g : H) {X : Matrix κ κ ℂ}
    (hX : X ∈ lieAlgebraOfIsClosed H hH) :
    (g.1 : Matrix κ κ ℂ) * X * (↑g.1⁻¹ : Matrix κ κ ℂ) ∈ lieAlgebraOfIsClosed H hH
```

**`Matrix.commutator_mem_lieAlgebraOfIsClosed`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/MatrixLieAlgebra.lean#L163).

> The Lie algebra is closed under the commutator. The conjugates
> `exp (t X) Y exp (−t X)` lie in the Lie algebra, a closed subspace, and so does their
> derivative `X Y − Y X` at `t = 0`.

```lean
lemma commutator_mem_lieAlgebraOfIsClosed {X Y : Matrix κ κ ℂ}
    (hX : X ∈ lieAlgebraOfIsClosed H hH) (hY : Y ∈ lieAlgebraOfIsClosed H hH) :
    X * Y - Y * X ∈ lieAlgebraOfIsClosed H hH
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [The Lie product formula](analysis-normed-algebra-lieproductformula.md)

## Sources

- [PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/MatrixLieAlgebra.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/MatrixLieAlgebra.lean)
