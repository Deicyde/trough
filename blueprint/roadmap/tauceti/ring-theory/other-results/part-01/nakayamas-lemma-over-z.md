---
declaration: theorem
origin: cited
lean: Submodule.eq_bot_of_forall_prime_le_smul, Module.exists_finset_card_le_finrank_and_smul_mem_span, IsIdempotentElem.exists_smul_eq_mul_of_mul_sub_smul_mem, TauCeti.maximalIdeal_eq_span_range_of_span_eq_top, Submodule.exists_sub_prod_mem_and_smul_eq_zero, Submodule.eq_bot_of_forall_isMaximal_le_smul
statement: formalized
proof: formalized
---

# Nakayama's lemma over `ℤ`

A finitely generated subgroup `N` of an abelian group with
`N ≤ p • N` for every prime `p` is zero.

```lean
Submodule.eq_bot_of_forall_prime_le_smul.{u_4} {M : Type u_4} [AddCommGroup M] {N : Submodule ℤ M}
  (hN : N.FG) (h : ∀ (p : ℕ), Nat.Prime p → N ≤ Ideal.span {↑p} • N) : N = ⊥
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Submodule.eq_bot_of_forall_prime_le_smul`](https://taucetiproject.org/docs/TauCeti/RingTheory/Finiteness/Nakayama.html#Submodule.eq_bot_of_forall_prime_le_smul).

## Other forms

**Nakayama's lemma at a field-valued point.** Formalized in Tau Ceti as [`Module.exists_finset_card_le_finrank_and_smul_mem_span`](https://taucetiproject.org/docs/TauCeti/RingTheory/Finiteness/Nakayama.html#Module.exists_finset_card_le_finrank_and_smul_mem_span).

```lean
Module.exists_finset_card_le_finrank_and_smul_mem_span.{u_1, u_2, u_3} {R : Type u_1} {M : Type u_2}
  {F : Type u_3} [CommRing R] [AddCommGroup M] [_root_.Module R M] [Module.Finite R M] [Field F]
  [Algebra R F] :
  ∃ s,
    s.card ≤ Module.finrank F (TensorProduct R F M) ∧
      ∃ r, (algebraMap R F) r ≠ 0 ∧ ∀ (x : M), r • x ∈ Submodule.span R ↑s
```

**Nakayama's lemma for an idempotent.** Formalized in Tau Ceti as [`IsIdempotentElem.exists_smul_eq_mul_of_mul_sub_smul_mem`](https://taucetiproject.org/docs/TauCeti/RingTheory/Idempotents/Jacobson.html#IsIdempotentElem.exists_smul_eq_mul_of_mul_sub_smul_mem).

```lean
IsIdempotentElem.exists_smul_eq_mul_of_mul_sub_smul_mem.{u_2, u_3} {S : Type u_2} {T : Type u_3}
  [CommRing S] [CommRing T] [Algebra S T] [Module.Finite S T] {J : Ideal S} (hJ : J ≤ ⊥.jacobson)
  {e : T} (he : IsIdempotentElem e)
  (h : ∀ (x : T), ∃ s, e * x - s • e ∈ Ideal.map (algebraMap S T) J) (x : T) : ∃ s, s • e = e * x
```

**Nakayama's lemma in coordinates.** Formalized in Tau Ceti as [`TauCeti.maximalIdeal_eq_span_range_of_span_eq_top`](https://taucetiproject.org/docs/TauCeti/RingTheory/LocalRing/Coordinates.html#TauCeti.maximalIdeal_eq_span_range_of_span_eq_top).

```lean
TauCeti.maximalIdeal_eq_span_range_of_span_eq_top.{u_1, u_2, u_3, u_4} {R : Type u_1} {Q : Type u_2}
  {ι : Type u_3} {κ : Type u_4} [CommSemiring R] [CommRing Q] [Algebra R Q] [IsLocalRing Q]
  [DecidableEq ι] {x : ι → Q} {D : ι → Derivation R Q Q} [Finite ι] [Finite κ]
  (hx : IsLocalRing.maximalIdeal Q = Ideal.span (Set.range x))
  (hD : ∀ (i j : ι), (D i) (x j) = if i = j then 1 else 0) {w : κ → Q}
  (hw : ∀ (k : κ), w k ∈ IsLocalRing.maximalIdeal Q)
  (h :
    Submodule.span (IsLocalRing.ResidueField Q)
        (Set.range fun k i => (IsLocalRing.residue Q) ((D i) (w k))) =
      ⊤) :
  IsLocalRing.maximalIdeal Q = Ideal.span (Set.range w)
```

**Nakayama's lemma with weighted generators.** Formalized in Tau Ceti as [`Submodule.exists_sub_prod_mem_and_smul_eq_zero`](https://taucetiproject.org/docs/TauCeti/RingTheory/Finiteness/Nakayama.html#Submodule.exists_sub_prod_mem_and_smul_eq_zero).

```lean
Submodule.exists_sub_prod_mem_and_smul_eq_zero.{u_1, u_2, u_3} {R : Type u_1} {M : Type u_2}
  {ι : Type u_3} [CommRing R] [AddCommGroup M] [_root_.Module R M] [Fintype ι] (I : Ideal R)
  {b : ι → M} (hb : Submodule.span R (Set.range b) = ⊤) (e : ι → R)
  (he : ∀ (i : ι), e i • b i ∈ I • ⊤) : ∃ r, r - ∏ i, e i ∈ I ∧ ∀ (m : M), r • m = 0
```

**Nakayama's lemma, globally.** Formalized in Tau Ceti as [`Submodule.eq_bot_of_forall_isMaximal_le_smul`](https://taucetiproject.org/docs/TauCeti/RingTheory/Finiteness/Nakayama.html#Submodule.eq_bot_of_forall_isMaximal_le_smul).

```lean
Submodule.eq_bot_of_forall_isMaximal_le_smul.{u_1, u_2} {R : Type u_1} {M : Type u_2} [CommRing R]
  [AddCommGroup M] [_root_.Module R M] {N : Submodule R M} (hN : N.FG)
  (h : ∀ (m : Ideal R), m.IsMaximal → N ≤ m • N) : N = ⊥
```

## Sources

- [Tau Ceti documentation: `Submodule.eq_bot_of_forall_prime_le_smul`](https://taucetiproject.org/docs/TauCeti/RingTheory/Finiteness/Nakayama.html#Submodule.eq_bot_of_forall_prime_le_smul)
- [Source of `Submodule.eq_bot_of_forall_prime_le_smul` in TauCeti/RingTheory/Finiteness/Nakayama.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Finiteness/Nakayama.lean#L116)
