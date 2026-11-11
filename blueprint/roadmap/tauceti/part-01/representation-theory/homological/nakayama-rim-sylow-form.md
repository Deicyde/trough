---
declaration: theorem
origin: cited
lean: Rep.projective_of_isZero_res_sylow, Rep.projective_of_isZero_res, Rep.projective_ker_of_isZero_res
statement: formalized
proof: formalized
---

# Nakayama–Rim, Sylow form

**Nakayama–Rim, Sylow form** (Serre, *Local Fields*, IX §§3–5; Rim, Ann. of Math. 69 (1959)).
Let `k` be a commutative ring, `G` a finite group, and `A` a representation of `G` on a
projective `k`-module. Suppose that for each prime `p` dividing `|G|` some Sylow `p`-subgroup `P`
satisfies: `p` is a unit in `k`, or `pk` is a maximal ideal, multiplication by `p` is injective
on `A`, and `H_Tate⁰(P, A) = H_Tate⁻¹(P, A) = 0`. Then `A` is projective over `k[G]`.

```lean
Rep.projective_of_isZero_res_sylow.{u} {k G : Type u} [CommRing k] [Group G] [Finite G]
  (A : Rep.{u, u, u} k G) [Module.Projective k ↑A]
  (h :
    ∀ (p : ℕ),
      Nat.Prime p →
        p ∣ Nat.card G →
          ∃ P x,
            IsUnit ↑p ∨
              (Ideal.span {↑p}).IsMaximal ∧
                (∀ (v : ↑A), ↑p • v = 0 → v = 0) ∧
                  CategoryTheory.Limits.IsZero (tateCohomology (Rep.res (↑P).subtype A) 0) ∧
                    CategoryTheory.Limits.IsZero (tateCohomology (Rep.res (↑P).subtype A) (-1))) :
  Module.Projective (MonoidAlgebra k G) A.ρ.asModule
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Schanuel's lemma in automorphism form](../../algebra/part-02/module/schanuels-lemma-in-automorphism-form.md)

## Lean

Formalized in Tau Ceti as [`Rep.projective_of_isZero_res_sylow`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/TateCohomology/Projective/Basic.html#Rep.projective_of_isZero_res_sylow).

## Other forms

**Nakayama–Rim, lattice form.** Formalized in Tau Ceti as [`Rep.projective_of_isZero_res`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/TateCohomology/Projective/Basic.html#Rep.projective_of_isZero_res).

```lean
Rep.projective_of_isZero_res.{u} {k G : Type u} [CommRing k] [Group G] [Finite G] [IsDomain k]
  [CharZero k] (hk : ∀ (p : ℕ), Nat.Prime p → IsUnit ↑p ∨ (Ideal.span {↑p}).IsMaximal)
  (A : Rep.{u, u, u} k G) [Module.Projective k ↑A]
  (hA :
    ∀ (S : Subgroup G) [inst : Fintype ↥S] (n : ℤ),
      CategoryTheory.Limits.IsZero (tateCohomology (Rep.res S.subtype A) n)) :
  Module.Projective (MonoidAlgebra k G) A.ρ.asModule
```

**Nakayama–Rim: cohomological triviality gives projective dimension at most one.** Formalized in Tau Ceti as [`Rep.projective_ker_of_isZero_res`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/TateCohomology/NakayamaRim.html#Rep.projective_ker_of_isZero_res).

```lean
Rep.projective_ker_of_isZero_res.{u, u_1} {k G : Type u} [CommRing k] [Group G] [Finite G]
  [IsDomain k] [IsPrincipalIdealRing k] [CharZero k]
  (hk : ∀ (p : ℕ), Nat.Prime p → IsUnit ↑p ∨ (Ideal.span {↑p}).IsMaximal) (A : Rep.{u, u, u} k G)
  (hA :
    ∀ (S : Subgroup G) [inst : Fintype ↥S] (n : ℤ),
      CategoryTheory.Limits.IsZero (tateCohomology (Rep.res S.subtype A) n))
  {P : Type u_1} [AddCommGroup P] [_root_.Module (MonoidAlgebra k G) P]
  [Module.Projective (MonoidAlgebra k G) P] (f : P →ₗ[MonoidAlgebra k G] A.ρ.asModule)
  (hf : Function.Surjective ⇑f) : Module.Projective (MonoidAlgebra k G) ↥f.ker
```

## Sources

- [Tau Ceti documentation: `Rep.projective_of_isZero_res_sylow`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/TateCohomology/Projective/Basic.html#Rep.projective_of_isZero_res_sylow)
- [Source of `Rep.projective_of_isZero_res_sylow` in TauCeti/RepresentationTheory/Homological/TateCohomology/Projective/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Homological/TateCohomology/Projective/Basic.lean#L180)
