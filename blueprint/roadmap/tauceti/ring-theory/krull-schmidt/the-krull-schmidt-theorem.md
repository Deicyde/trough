---
declaration: theorem
origin: cited
lean: TauCeti.exists_equiv_linearEquiv_of_iSupIndep, TauCeti.exists_equiv_linearEquiv_of_finset, TauCeti.exists_equiv_linearEquiv_of_isLocalRing_end, TauCeti.exists_equiv_linearEquiv_of_directSum, TauCeti.exists_equiv_linearEquiv_of_directSum_of_isLocalRing_end, TauCeti.exists_equiv_linearEquiv_of_directSumEquiv
statement: formalized
proof: formalized
---

# The Krull-Schmidt theorem

Two decompositions of a module of finite length into
indecomposable submodules are matched by a bijection of their index sets under which corresponding
summands are isomorphic.

The index types need not carry finiteness instances: independence and the nonzero summands force
them to be finite because the ambient module is Noetherian.

Fitting's lemma makes the endomorphism ring of each summand local, as needed by
`TauCeti.exists_equiv_linearEquiv_of_isLocalRing_end`. Existence of such a decomposition is
`TauCeti.exists_indecomposable_decomposition`.

```lean
TauCeti.exists_equiv_linearEquiv_of_iSupIndep.{u, v, w, x} {A : Type u} [Ring A] {M : Type v}
  [AddCommGroup M] [_root_.Module A M] [IsNoetherian A M] [IsArtinian A M] {ι : Type w} {κ : Type x}
  {P : ι → Submodule A M} {Q : κ → Submodule A M} (hP : iSupIndep P) (hPt : ⨆ i, P i = ⊤)
  (hPind : ∀ (i : ι), TauCeti.IsIndecomposableModule A ↥(P i)) (hQ : iSupIndep Q)
  (hQt : ⨆ j, Q j = ⊤) (hQind : ∀ (j : κ), TauCeti.IsIndecomposableModule A ↥(Q j)) :
  ∃ e, ∀ (i : ι), Nonempty (↥(P i) ≃ₗ[A] ↥(Q (e i)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Azumaya's exchange lemma](azumayas-exchange-lemma.md)
- [Fitting's lemma](fittings-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_equiv_linearEquiv_of_iSupIndep`](https://taucetiproject.org/docs/TauCeti/RingTheory/KrullSchmidt/Uniqueness.html#TauCeti.exists_equiv_linearEquiv_of_iSupIndep).

## Other forms

**The Krull-Schmidt theorem, in the `Finset` packaging that `TauCeti.exists_indecomposable_decomposition` produces.** Formalized in Tau Ceti as [`TauCeti.exists_equiv_linearEquiv_of_finset`](https://taucetiproject.org/docs/TauCeti/RingTheory/KrullSchmidt/Uniqueness.html#TauCeti.exists_equiv_linearEquiv_of_finset).

```lean
TauCeti.exists_equiv_linearEquiv_of_finset.{u, v} {A : Type u} [Ring A] {M : Type v}
  [AddCommGroup M] [_root_.Module A M] (hM : IsFiniteLength A M) {s t : Finset (Submodule A M)}
  (hs : ∀ N ∈ s, TauCeti.IsIndecomposableModule A ↥N) (hsi : DirectSum.IsInternal fun N => ↑N)
  (ht : ∀ N ∈ t, TauCeti.IsIndecomposableModule A ↥N) (hti : DirectSum.IsInternal fun N => ↑N) :
  ∃ e, ∀ (N : ↥s), Nonempty (↥↑N ≃ₗ[A] ↥↑(e N))
```

**The Krull-Schmidt theorem, in Azumaya's generality.** Formalized in Tau Ceti as [`TauCeti.exists_equiv_linearEquiv_of_isLocalRing_end`](https://taucetiproject.org/docs/TauCeti/RingTheory/KrullSchmidt/Uniqueness.html#TauCeti.exists_equiv_linearEquiv_of_isLocalRing_end).

```lean
TauCeti.exists_equiv_linearEquiv_of_isLocalRing_end.{u, v, w, x} {A : Type u} [Ring A] {M : Type v}
  [AddCommGroup M] [_root_.Module A M] {ι : Type w} {κ : Type x} [Finite ι] [Finite κ]
  {P : ι → Submodule A M} {Q : κ → Submodule A M} (hP : iSupIndep P) (hPt : ⨆ i, P i = ⊤)
  (hPloc : ∀ (i : ι), IsLocalRing (Module.End A ↥(P i))) (hQ : iSupIndep Q) (hQt : ⨆ j, Q j = ⊤)
  (hQind : ∀ (j : κ), TauCeti.IsIndecomposableModule A ↥(Q j)) :
  ∃ e, ∀ (i : ι), Nonempty (↥(P i) ≃ₗ[A] ↥(Q (e i)))
```

**The Krull-Schmidt theorem for external direct sums.** Formalized in Tau Ceti as [`TauCeti.exists_equiv_linearEquiv_of_directSum`](https://taucetiproject.org/docs/TauCeti/RingTheory/KrullSchmidt/DirectSum.html#TauCeti.exists_equiv_linearEquiv_of_directSum).

```lean
TauCeti.exists_equiv_linearEquiv_of_directSum.{u, v, w, x, y, z} {A : Type u} [Ring A] {M : Type v}
  [AddCommGroup M] [_root_.Module A M] {ι : Type w} {κ : Type x} {N : ι → Type y}
  [(i : ι) → AddCommGroup (N i)] [(i : ι) → _root_.Module A (N i)] {Q : κ → Type z}
  [(j : κ) → AddCommGroup (Q j)] [(j : κ) → _root_.Module A (Q j)] [IsNoetherian A M]
  [IsArtinian A M] (eN : M ≃ₗ[A] DirectSum ι fun i => N i) (eQ : M ≃ₗ[A] DirectSum κ fun j => Q j)
  (hN : ∀ (i : ι), TauCeti.IsIndecomposableModule A (N i))
  (hQ : ∀ (j : κ), TauCeti.IsIndecomposableModule A (Q j)) :
  ∃ e, ∀ (i : ι), Nonempty (N i ≃ₗ[A] Q (e i))
```

**The Krull-Schmidt theorem for external direct sums, in Azumaya's generality.** Formalized in Tau Ceti as [`TauCeti.exists_equiv_linearEquiv_of_directSum_of_isLocalRing_end`](https://taucetiproject.org/docs/TauCeti/RingTheory/KrullSchmidt/DirectSum.html#TauCeti.exists_equiv_linearEquiv_of_directSum_of_isLocalRing_end).

```lean
TauCeti.exists_equiv_linearEquiv_of_directSum_of_isLocalRing_end.{u, v, w, x, y, z} {A : Type u}
  [Ring A] {M : Type v} [AddCommGroup M] [_root_.Module A M] {ι : Type w} {κ : Type x}
  {N : ι → Type y} [(i : ι) → AddCommGroup (N i)] [(i : ι) → _root_.Module A (N i)] {Q : κ → Type z}
  [(j : κ) → AddCommGroup (Q j)] [(j : κ) → _root_.Module A (Q j)] [Finite ι] [Finite κ]
  (eN : M ≃ₗ[A] DirectSum ι fun i => N i) (eQ : M ≃ₗ[A] DirectSum κ fun j => Q j)
  (hN : ∀ (i : ι), IsLocalRing (Module.End A (N i)))
  (hQ : ∀ (j : κ), TauCeti.IsIndecomposableModule A (Q j)) :
  ∃ e, ∀ (i : ι), Nonempty (N i ≃ₗ[A] Q (e i))
```

**The Krull-Schmidt theorem for two abstract families of summands.** Formalized in Tau Ceti as [`TauCeti.exists_equiv_linearEquiv_of_directSumEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/KrullSchmidt/DirectSum.html#TauCeti.exists_equiv_linearEquiv_of_directSumEquiv).

```lean
TauCeti.exists_equiv_linearEquiv_of_directSumEquiv.{u, w, x, y, z} {A : Type u} [Ring A]
  {ι : Type w} {κ : Type x} {N : ι → Type y} [(i : ι) → AddCommGroup (N i)]
  [(i : ι) → _root_.Module A (N i)] {Q : κ → Type z} [(j : κ) → AddCommGroup (Q j)]
  [(j : κ) → _root_.Module A (Q j)] [Finite ι] [Finite κ]
  (e : (DirectSum ι fun i => N i) ≃ₗ[A] DirectSum κ fun j => Q j)
  (hN : ∀ (i : ι), IsLocalRing (Module.End A (N i)))
  (hQ : ∀ (j : κ), TauCeti.IsIndecomposableModule A (Q j)) :
  ∃ f, ∀ (i : ι), Nonempty (N i ≃ₗ[A] Q (f i))
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_equiv_linearEquiv_of_iSupIndep`](https://taucetiproject.org/docs/TauCeti/RingTheory/KrullSchmidt/Uniqueness.html#TauCeti.exists_equiv_linearEquiv_of_iSupIndep)
- [Source of `TauCeti.exists_equiv_linearEquiv_of_iSupIndep` in TauCeti/RingTheory/KrullSchmidt/Uniqueness.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/KrullSchmidt/Uniqueness.lean#L176)
