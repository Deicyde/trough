---
declaration: theorem
origin: cited
lean: Ideal.exists_pow_add_smul_inf_eq_pow_smul
statement: formalized
proof: formalized
---

# Artin–Rees for a finitely generated submodule

If `N₀` is a finitely generated submodule
over a noetherian ring, there is a shift `k` such that `I ^ (n + k) • N₀ ⊓ L` equals
`I ^ n • (I ^ k • N₀ ⊓ L)` for every submodule `L` and every `n`. The ambient module need not be
finite: only `N₀` is, so Mathlib's `Ideal.exists_pow_inf_eq_pow_smul` is applied inside `N₀`.
In particular `I ^ (n + k) • N₀ ⊓ L ≤ I ^ n • L`; when `L ≤ N₀`, this shows that the
filtration `N₀` induces on `L` is cofinal in the `I`-adic filtration of `L`.

```lean
Ideal.exists_pow_add_smul_inf_eq_pow_smul.{u_1, u_2} {R : Type u_1} [CommRing R] {M : Type u_2}
  [AddCommGroup M] [_root_.Module R M] [IsNoetherianRing R] (I : Ideal R) {N₀ : Submodule R M}
  (hN₀ : N₀.FG) (L : Submodule R M) :
  ∃ k, ∀ (n : ℕ), I ^ (n + k) • N₀ ⊓ L = I ^ n • (I ^ k • N₀ ⊓ L)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Ideal.exists_pow_add_smul_inf_eq_pow_smul`](https://taucetiproject.org/docs/TauCeti/RingTheory/Ideal/ArtinRees.html#Ideal.exists_pow_add_smul_inf_eq_pow_smul).

## Sources

- [Tau Ceti documentation: `Ideal.exists_pow_add_smul_inf_eq_pow_smul`](https://taucetiproject.org/docs/TauCeti/RingTheory/Ideal/ArtinRees.html#Ideal.exists_pow_add_smul_inf_eq_pow_smul)
- [Source of `Ideal.exists_pow_add_smul_inf_eq_pow_smul` in TauCeti/RingTheory/Ideal/ArtinRees.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Ideal/ArtinRees.lean#L124)
