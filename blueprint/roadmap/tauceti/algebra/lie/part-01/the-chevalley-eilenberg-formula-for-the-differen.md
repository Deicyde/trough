---
declaration: theorem
origin: cited
lean: TauCeti.LieModule.Cohomology.d_succ_apply
statement: formalized
proof: formalized
---

# The Chevalley–Eilenberg formula for the differential of a cochain of positive degree

`(d ω)(x₀, …, xₙ₊₁) = ∑ i, (-1)^i ⁅xᵢ, ω(…, x̂ᵢ, …)⁆ + ∑_{i < j} (-1)^(i + j) ω(⁅xᵢ, xⱼ⁆, …)`,
where the pairs `i < j` are written as `(i.castSucc, j.succ)` with `i ≤ j`.

```lean
TauCeti.LieModule.Cohomology.d_succ_apply.{u_1, u_2, u_3} {R : Type u_1} [CommRing R] {L : Type u_2}
  [LieRing L] [LieAlgebra R L] {M : Type u_3} [AddCommGroup M] [_root_.Module R M]
  [LieRingModule L M] [LieModule R L M] {n : ℕ} (ω : L [⋀^Fin (n + 1)]→ₗ[R] M)
  (v : Fin (n + 2) → L) :
  ((TauCeti.LieModule.Cohomology.d R L M (n + 1)) ω) v =
    ∑ i, (-1) ^ ↑i • ⁅v i, ω (i.removeNth v)⁆ +
      ∑ i,
        ∑ j ≥ i,
          (-1) ^ (↑i + ↑j + 1) •
            ω (Matrix.vecCons ⁅v i.castSucc, v j.succ⁆ (j.removeNth (i.castSucc.removeNth v)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartan's formula `ι_x d ω = L_x ω - d ι_x ω`](cartans-formula-x-d-l-x-d-x.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LieModule.Cohomology.d_succ_apply`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.html#TauCeti.LieModule.Cohomology.d_succ_apply).

## Sources

- [Tau Ceti documentation: `TauCeti.LieModule.Cohomology.d_succ_apply`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.html#TauCeti.LieModule.Cohomology.d_succ_apply)
- [Source of `TauCeti.LieModule.Cohomology.d_succ_apply` in TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.lean#L254)
