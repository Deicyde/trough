---
declaration: theorem
origin: cited
lean: LinearMap.BilinForm.pairwise_of_apply_self_eq_zero
statement: formalized
proof: formalized
---

# Disjointness on a square-zero ray

Let `B` be the intersection form and let every
candidate of `T` have class `m c • A₀`, where `A₀ · A₀ = 0`. If distinct candidates of `T` with
intersection number zero are compatible, as positivity of intersections gives for distinct
pseudoholomorphic images, then the candidates of `T` are pairwise compatible.

```lean
LinearMap.BilinForm.pairwise_of_apply_self_eq_zero.{u_1, u_2} {ι : Type u_1} {H : Type u_2}
  [AddCommGroup H] {r : ι → ι → Prop} {cls : ι → H} {T : Set ι} {A₀ : H} {m : ι → ℕ}
  (B : LinearMap.BilinForm ℤ H) (hA₀ : (B A₀) A₀ = 0) (hcls : ∀ c ∈ T, cls c = m c • A₀)
  (hr : ∀ a ∈ T, ∀ b ∈ T, a ≠ b → (B (cls a)) (cls b) = 0 → r a b) : T.Pairwise r
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.BilinForm.pairwise_of_apply_self_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/ConfigurationCount.html#LinearMap.BilinForm.pairwise_of_apply_self_eq_zero).

## Sources

- [Tau Ceti documentation: `LinearMap.BilinForm.pairwise_of_apply_self_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/ConfigurationCount.html#LinearMap.BilinForm.pairwise_of_apply_self_eq_zero)
- [Source of `LinearMap.BilinForm.pairwise_of_apply_self_eq_zero` in TauCeti/Geometry/Symplectic/JHolomorphic/ConfigurationCount.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/JHolomorphic/ConfigurationCount.lean#L579)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TaubesGromov/STATUS.md)
