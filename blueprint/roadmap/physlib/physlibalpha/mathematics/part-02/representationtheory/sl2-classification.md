---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.stringVecs, PhyslibAlpha.Sl2.string_hasEigenvector, PhyslibAlpha.Sl2.string_weight_injective, PhyslibAlpha.Sl2.string_linearIndependent, PhyslibAlpha.Sl2.stringSpan, PhyslibAlpha.Sl2.stringPow_mem_span, PhyslibAlpha.Sl2.lie_e_string_mem, PhyslibAlpha.Sl2.lie_f_string_mem
statement: formalized
proof: formalized
---

# Classification of irreducible sl₂ modules

The module `PhyslibAlpha.Mathematics.RepresentationTheory.Sl2.Classification`, [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean): 32 declarations, 32 with a docstring.

> Constructs the primitive-vector string basis and classifies finite-dimensional irreducible modules.

## i. Overview

> Mathlib’s primitive-vector formulas give a lowering string of nonzero vectors with distinct
> weights. For an irreducible module, its invariant span is the whole space, so the string is a
> basis. Comparing its action with the explicit standard module yields a linear equivalence
> intertwining the generated Lie subalgebra.

## ii. Key results

> - `string_isBasis` constructs the lowering-string basis.
> - `finrank_eq_succ` reads off the dimension from the highest weight.
> - `classification` identifies an irreducible module with the standard module.

## iv. References

> - Mathlib, `Mathlib.Algebra.Lie.Sl2`.

## A. Primitive strings and classification

**`PhyslibAlpha.Sl2.stringVecs`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L50).

> The vectors `m, fm, …, fⁿm` of the primitive-vector string, indexed by `Fin (n+1)`.

```lean
def stringVecs (f : L) (m : M) (n : ℕ) (k : Fin (n + 1)) : M
```

**`PhyslibAlpha.Sl2.string_hasEigenvector`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L54).

> Each vector in a primitive lowering string is a nonzero eigenvector of `h`.

```lean
lemma string_hasEigenvector [CharZero K] {t : IsSl2Triple h e f}
    (P : t.HasPrimitiveVectorWith m (n : K)) (k : Fin (n + 1)) :
    (LieModule.toEnd K L M h).HasEigenvector ((n : K) - 2 * (k : ℕ))
      (stringVecs (K := K) f m n k)
```

**`PhyslibAlpha.Sl2.string_weight_injective`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L64).

> The weights `n - 2k` of a lowering string are pairwise distinct in characteristic zero.

```lean
lemma string_weight_injective [CharZero K] {n : ℕ} :
    Function.Injective (fun k : Fin (n + 1) => (n : K) - 2 * (k : ℕ))
```

**`PhyslibAlpha.Sl2.string_linearIndependent`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L73).

> The lowering string is linearly independent because its weights are distinct.

```lean
lemma string_linearIndependent [CharZero K] {t : IsSl2Triple h e f}
    (P : t.HasPrimitiveVectorWith m (n : K)) :
    LinearIndependent K (stringVecs (K := K) f m n)
```

**`PhyslibAlpha.Sl2.stringSpan`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L81).

> The span of the primitive-vector string, as a plain `K`-submodule.

```lean
def stringSpan (f : L) (m : M) (n : ℕ) : Submodule K M
```

**`PhyslibAlpha.Sl2.stringPow_mem_span`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L85).

> Every power of the lowering operator lies in the truncated string span.

```lean
lemma stringPow_mem_span [CharZero K] [FiniteDimensional K M] {t : IsSl2Triple h e f}
    (P : t.HasPrimitiveVectorWith m (n : K)) (k : ℕ) :
    (LieModule.toEnd K L M f ^ k) m ∈ stringSpan (K := K) f m n
```

**`PhyslibAlpha.Sl2.lie_e_string_mem`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L101).

> The raising operator preserves the span of a primitive lowering string.

```lean
lemma lie_e_string_mem [CharZero K] [FiniteDimensional K M] {t : IsSl2Triple h e f}
    (P : t.HasPrimitiveVectorWith m (n : K)) (k : Fin (n + 1)) :
    ⁅e, stringVecs (K := K) f m n k⁆ ∈ stringSpan (K := K) f m n
```

**`PhyslibAlpha.Sl2.lie_f_string_mem`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L116).

> The raising operator preserves the string span on `f`-powers.

```lean
lemma lie_f_string_mem [CharZero K] [FiniteDimensional K M] {t : IsSl2Triple h e f}
    (P : t.HasPrimitiveVectorWith m (n : K)) (k : Fin (n + 1)) :
    ⁅f, stringVecs (K := K) f m n k⁆ ∈ stringSpan (K := K) f m n
```

**`PhyslibAlpha.Sl2.lie_h_string_mem`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L124).

> The Cartan operator preserves the string span.

```lean
lemma lie_h_string_mem {t : IsSl2Triple h e f}
    (P : t.HasPrimitiveVectorWith m (n : K)) (k : Fin (n + 1)) :
    ⁅h, stringVecs (K := K) f m n k⁆ ∈ stringSpan (K := K) f m n
```

**`PhyslibAlpha.Sl2.lie_generator_string_mem`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L132).

> Each generator of the triple preserves the lowering-string span.

```lean
lemma lie_generator_string_mem [CharZero K] [FiniteDimensional K M] {t : IsSl2Triple h e f}
    (P : t.HasPrimitiveVectorWith m (n : K))
    (x : ↥(t.toLieSubalgebra (R := K))) (k : Fin (n + 1)) :
    ⁅x, stringVecs (K := K) f m n k⁆ ∈ stringSpan (K := K) f m n
```

**`PhyslibAlpha.Sl2.exists_stringLieSubmodule`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L146).

> The lowering string spans a submodule for the Lie subalgebra generated by `t`.
> The finite-dimensional hypothesis supplies the relation that closes the string after `n + 1`
> lowering steps.

```lean
lemma exists_stringLieSubmodule [CharZero K] [FiniteDimensional K M] {t : IsSl2Triple h e f}
    (P : t.HasPrimitiveVectorWith m (n : K)) :
    ∃ N : LieSubmodule K ↥(t.toLieSubalgebra (R := K)) M,
      (N : Submodule K M) = stringSpan f m n
```

**`PhyslibAlpha.Sl2.stringSpan_eq_top`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L161).

> Irreducibility makes the nonzero lowering-string submodule equal to the whole module.

```lean
lemma stringSpan_eq_top {t : IsSl2Triple h e f}
    [LieModule.IsIrreducible K ↥(t.toLieSubalgebra (R := K)) M]
    (P : t.HasPrimitiveVectorWith m (n : K)) (N : LieSubmodule K ↥(t.toLieSubalgebra (R := K)) M)
    (hN : (N : Submodule K M) = stringSpan f m n) : N = ⊤
```

**`PhyslibAlpha.Sl2.string_isBasis`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L176).

> In an irreducible module, the lowering string is independent and spans.

```lean
lemma string_isBasis [CharZero K] [FiniteDimensional K M] {t : IsSl2Triple h e f}
    [LieModule.IsIrreducible K ↥(t.toLieSubalgebra (R := K)) M]
    (P : t.HasPrimitiveVectorWith m (n : K)) :
    LinearIndependent K (stringVecs (K := K) f m n) ∧
      Submodule.span K (Set.range (stringVecs (K := K) f m n)) = ⊤
```

**`PhyslibAlpha.Sl2.finrank_eq_succ`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L188).

> Basis theorem, dimension count.

```lean
lemma finrank_eq_succ [CharZero K] [FiniteDimensional K M] {t : IsSl2Triple h e f}
    [LieModule.IsIrreducible K ↥(t.toLieSubalgebra (R := K)) M]
    (P : t.HasPrimitiveVectorWith m (n : K)) :
    Module.finrank K M = n + 1
```

**`PhyslibAlpha.Sl2.stringBasis`**, a def, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L197).

> The basis of an irreducible module obtained by lowering a primitive vector.

```lean
noncomputable def stringBasis [CharZero K] [FiniteDimensional K M]
    {t : IsSl2Triple h e f}
    [LieModule.IsIrreducible K ↥(t.toLieSubalgebra (R := K)) M]
    (P : t.HasPrimitiveVectorWith m (n : K)) : Module.Basis (Fin (n + 1)) K M
```

**`PhyslibAlpha.Sl2.stringEquiv`**, a def, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L204).

> The linear equivalence sending the lowering-string basis to the coordinate basis.

```lean
noncomputable def stringEquiv [CharZero K] [FiniteDimensional K M]
    {t : IsSl2Triple h e f}
    [LieModule.IsIrreducible K ↥(t.toLieSubalgebra (R := K)) M]
    (P : t.HasPrimitiveVectorWith m (n : K)) : M ≃ₗ[K] StandardSl2Module K n
```

**`PhyslibAlpha.Sl2.stringEquiv_apply`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L212).

> The linear equivalence sends each lowering-string vector to the corresponding
> coordinate vector.

```lean
lemma stringEquiv_apply [CharZero K] [FiniteDimensional K M]
    {t : IsSl2Triple h e f}
    [LieModule.IsIrreducible K ↥(t.toLieSubalgebra (R := K)) M]
    (P : t.HasPrimitiveVectorWith m (n : K)) (i : Fin (n + 1)) :
    stringEquiv P (stringVecs (K := K) f m n i) = StandardSl2Module.v i
```

**`PhyslibAlpha.Sl2.stringEquiv_e_zero`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L230).

> The raising operators agree at the primitive vector.

```lean
lemma stringEquiv_e_zero :
    letI := standardSl2ModuleLieRingModule (K := K) (n := n) t
    stringEquiv P ⁅eSub (K := K) t, stringVecs (K := K) f m n 0⁆ =
      ⁅eSub (K := K) t, StandardSl2Module.v (K := K) (n := n) 0⁆
```

**`PhyslibAlpha.Sl2.stringEquiv_e_succ`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L240).

> The raising operators agree at the string vector with index `j + 1`.

```lean
lemma stringEquiv_e_succ (j : ℕ) (hj : j < n) :
    letI := standardSl2ModuleLieRingModule (K := K) (n := n) t
    stringEquiv P ⁅eSub (K := K) t, stringVecs (K := K) f m n ⟨j + 1, by omega⟩⁆ =
      ⁅eSub (K := K) t, StandardSl2Module.v (K := K) (n := n) ⟨j + 1, by omega⟩⁆
```

**`PhyslibAlpha.Sl2.stringEquiv_e_pos`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L254).

> The raising operators agree at every positive string index.

```lean
lemma stringEquiv_e_pos (i : Fin (n + 1)) (hi : 0 < (i : ℕ)) :
    letI := standardSl2ModuleLieRingModule (K := K) (n := n) t
    stringEquiv P ⁅eSub (K := K) t, stringVecs (K := K) f m n i⁆ =
      ⁅eSub (K := K) t, StandardSl2Module.v (K := K) (n := n) i⁆
```

**`PhyslibAlpha.Sl2.equiv_comm_of_basis`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L264).

> A linear equivalence intertwines two endomorphisms if it does so on a basis.

```lean
lemma equiv_comm_of_basis {ι V : Type*} [AddCommGroup V] [Module K V]
    (b : Module.Basis ι K M) (Ψ : M ≃ₗ[K] V) (A : M →ₗ[K] M) (B : V →ₗ[K] V)
    (hb : ∀ i, Ψ (A (b i)) = B (Ψ (b i))) (w : M) : Ψ (A w) = B (Ψ w)
```

**`PhyslibAlpha.Sl2.stringEquiv_lie_of_basis`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L271).

> The coordinate equivalence intertwines `x` once it does so on the string basis.

```lean
lemma stringEquiv_lie_of_basis (x : ↥(t.toLieSubalgebra (R := K)))
    (hx : letI := standardSl2ModuleLieRingModule (K := K) (n := n) t
      ∀ i, stringEquiv P ⁅x, stringVecs (K := K) f m n i⁆ =
        ⁅x, StandardSl2Module.v (K := K) (n := n) i⁆) (w : M) :
    letI := standardSl2ModuleLieRingModule (K := K) (n := n) t
    stringEquiv P ⁅x, w⁆ = ⁅x, stringEquiv P w⁆
```

**`PhyslibAlpha.Sl2.stringEquiv_e`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L284).

> The coordinate equivalence intertwines the raising operator.

```lean
lemma stringEquiv_e (w : M) :
    letI := standardSl2ModuleLieRingModule (K := K) (n := n) t
    stringEquiv P ⁅eSub (K := K) t, w⁆ = ⁅eSub (K := K) t, stringEquiv P w⁆
```

**`PhyslibAlpha.Sl2.stringEquiv_f_last`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L295).

> The lowering operators agree at the last string vector.

```lean
lemma stringEquiv_f_last :
    letI := standardSl2ModuleLieRingModule (K := K) (n := n) t
    stringEquiv P ⁅fSub (K := K) t, stringVecs (K := K) f m n (Fin.last n)⁆ =
      ⁅fSub (K := K) t, StandardSl2Module.v (K := K) (n := n) (Fin.last n)⁆
```

**`PhyslibAlpha.Sl2.stringEquiv_f_lt`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L305).

> The lowering operators agree before the last string vector.

```lean
lemma stringEquiv_f_lt (i : Fin (n + 1)) (hi : (i : ℕ) < n) :
    letI := standardSl2ModuleLieRingModule (K := K) (n := n) t
    stringEquiv P ⁅fSub (K := K) t, stringVecs (K := K) f m n i⁆ =
      ⁅fSub (K := K) t, StandardSl2Module.v (K := K) (n := n) i⁆
```

**`PhyslibAlpha.Sl2.stringEquiv_f`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L316).

> The coordinate equivalence intertwines the lowering operator.

```lean
lemma stringEquiv_f (w : M) :
    letI := standardSl2ModuleLieRingModule (K := K) (n := n) t
    stringEquiv P ⁅fSub (K := K) t, w⁆ = ⁅fSub (K := K) t, stringEquiv P w⁆
```

**`PhyslibAlpha.Sl2.stringEquiv_h_basis`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L327).

> The Cartan operators agree on every string vector.

```lean
lemma stringEquiv_h_basis (i : Fin (n + 1)) :
    letI := standardSl2ModuleLieRingModule (K := K) (n := n) t
    stringEquiv P ⁅hSub (K := K) t, stringVecs (K := K) f m n i⁆ =
      ⁅hSub (K := K) t, StandardSl2Module.v (K := K) (n := n) i⁆
```

**`PhyslibAlpha.Sl2.stringEquiv_h`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L338).

> The coordinate equivalence intertwines the Cartan operator.

```lean
lemma stringEquiv_h (w : M) :
    letI := standardSl2ModuleLieRingModule (K := K) (n := n) t
    stringEquiv P ⁅hSub (K := K) t, w⁆ = ⁅hSub (K := K) t, stringEquiv P w⁆
```

**`PhyslibAlpha.Sl2.exists_decomp`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L345).

> Every element of the generated subalgebra is a combination of `e`, `f`, `h`.

```lean
lemma exists_decomp (x : ↥(t.toLieSubalgebra (R := K))) :
    ∃ c₁ c₂ c₃ : K, x = c₁ • eSub (K := K) t + c₂ • fSub (K := K) t + c₃ • hSub (K := K) t
```

**`PhyslibAlpha.Sl2.stringEquiv_lie`**, a lemma, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L353).

> The coordinate equivalence intertwines every element of the generated subalgebra.

```lean
lemma stringEquiv_lie (x : ↥(t.toLieSubalgebra (R := K))) (w : M) :
    letI := standardSl2ModuleLieRingModule (K := K) (n := n) t
    stringEquiv P ⁅x, w⁆ = ⁅x, stringEquiv P w⁆
```

**`PhyslibAlpha.Sl2.classification`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L366).

> A finite-dimensional irreducible module for the generated `sl₂` subalgebra is
> equivalent to a standard highest-weight module.

```lean
lemma classification [IsAlgClosed K] [CharZero K] [FiniteDimensional K M] (t : IsSl2Triple h e f)
    [LieModule.IsIrreducible K ↥(t.toLieSubalgebra (R := K)) M] :
    ∃ n : ℕ, letI := standardSl2ModuleLieRingModule (K := K) (n := n) t
      Nonempty (M ≃ₗ⁅K, ↥(t.toLieSubalgebra (R := K))⁆ StandardSl2Module K n)
```

**`PhyslibAlpha.Sl2.classification_n_eq_finrank_sub_one`**, a lemma, [line 385](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean#L385).

> Uniqueness of the highest weight: the `n` produced by
> `classification` is determined by `M` alone, namely `n = finrank K M - 1`.
>
> Unlike `classification`, irreducibility is not actually needed here: only the bare existence of
> some `K`-linear equivalence `M ≃ₗ[K] V(n)` (forgetting the Lie-module structure `hn` provides) is
> used, via a dimension count.

```lean
lemma classification_n_eq_finrank_sub_one [CharZero K]
    {t : IsSl2Triple h e f} {n : ℕ}
    (hn : letI := standardSl2ModuleLieRingModule (K := K) (n := n) t
      Nonempty (M ≃ₗ⁅K, ↥(t.toLieSubalgebra (R := K))⁆ StandardSl2Module K n)) :
    n = Module.finrank K M - 1
```

## Depends on

- [The standard sl₂ Lie module](sl2-basic.md)

## Sources

- [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Classification.lean)
