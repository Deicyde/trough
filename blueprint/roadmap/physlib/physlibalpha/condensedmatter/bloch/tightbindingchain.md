---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.hoppingMatrix, CondensedMatter.TightBindingChain.hopping_hoppingMatrix
statement: formalized
proof: formalized
---

# The tight binding chain as a finite periodic crystal

The module `PhyslibAlpha.CondensedMatter.Bloch.TightBindingChain`, [PhyslibAlpha/CondensedMatter/Bloch/TightBindingChain.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/Bloch/TightBindingChain.lean): 2 declarations, 2 with a docstring.

## i. Overview

> The tight binding chain of `N` sites with periodic boundary conditions is a finite periodic
> crystal with translation group `Fin N` and one orbital per cell. In the coordinates `⟪|x⟩, ψ⟫`
> its Hamiltonian is the hopping operator with the matrix `E0` on the site itself and `-t` to each
> of its two neighbours.

## ii. Key results

> - `hoppingMatrix` : the hopping matrices of the tight binding chain.
> - `hopping_hoppingMatrix` : the Hamiltonian of the tight binding chain is the hopping operator of
>   these matrices.

## iv. References

> None.

## A. The Hamiltonian as a hopping operator

**`CondensedMatter.TightBindingChain.hoppingMatrix`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/Bloch/TightBindingChain.lean#L55).

> The hopping matrices of the tight binding chain as a finite periodic crystal with one orbital
> per cell: `E0` on the site itself and `-t` to each of its two neighbours.

```lean
noncomputable def hoppingMatrix (r : Fin T.N) : Matrix (Fin 1) (Fin 1) ℂ
```

**`CondensedMatter.TightBindingChain.hopping_hoppingMatrix`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/Bloch/TightBindingChain.lean#L61).

> The Hamiltonian of the tight binding chain, in the coordinates `⟪|x⟩, ψ⟫`, is the hopping
> operator of the finite periodic crystal with the matrices `hoppingMatrix`.

```lean
lemma hopping_hoppingMatrix (ψ : T.HilbertSpace) :
    hopping T.hoppingMatrix (fun x _ => ⟪|x⟩, ψ⟫_ℂ) = fun x _ => ⟪|x⟩, T.hamiltonian ψ⟫_ℂ := by
  ext x i
  rw [hopping_apply, ← hamiltonian_hermitian, hamiltonian_apply_localizedState]
  simp only [hoppingMatrix, Matrix.smul_mulVec, Matrix.one_mulVec, Finset.sum_apply,
    Pi.smul_apply, smul_eq_mul, sub_mul, ite_mul, zero_mul, Finset.sum_sub_distrib,
    Finset.sum_ite_eq', Finset.mem_univ, ite_true, sub_zero, sub_neg_eq_add, inner_sub_left,
    inner_add_left, inner_smul_left, Complex.conj_ofReal]
  ring
```

## Depends on

- [The tight binding chain](../../../physlib/condensedmatter/tightbindingchain/basic.md)
- [The spectrum of a finite periodic crystal](finitebloch.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Bloch/TightBindingChain.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/CondensedMatter/Bloch/TightBindingChain.lean)
