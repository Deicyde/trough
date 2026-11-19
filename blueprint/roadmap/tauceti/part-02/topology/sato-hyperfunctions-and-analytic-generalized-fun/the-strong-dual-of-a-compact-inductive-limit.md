---
declaration: def
origin: cited
lean: TauCeti.dualProjectiveLimit.strongDualEquiv
statement: formalized
---

# The strong dual of a compact inductive limit

Let `L` be the inductive limit of a sequence
of normed spaces `B j` with weakly compact bonding maps, in particular with compact bonding maps,
and suppose that continuous functionals separate the points of `L`. Then precomposition with the
maps `ι j` is an isomorphism of topological vector spaces from the strong dual `L′_b` onto the
projective limit `lim_j B j′` of the dual Banach spaces.

```lean
TauCeti.dualProjectiveLimit.strongDualEquiv.{u_1, u_2, u_3} {𝕜 : Type u_1} [RCLike 𝕜]
  {B : ℕ → Type u_2} [(n : ℕ) → NormedAddCommGroup (B n)] [(n : ℕ) → NormedSpace 𝕜 (B n)]
  {T : (n : ℕ) → B n →L[𝕜] B (n + 1)} {L : Type u_3} [AddCommGroup L] [_root_.Module 𝕜 L]
  [TopologicalSpace L] {ι : (n : ℕ) → B n →L[𝕜] L} [SeparatingDual 𝕜 L]
  (hT : ∀ (n : ℕ), (T n).IsWeaklyCompact) (hι : ∀ (n : ℕ), ι (n + 1) ∘SL T n = ι n)
  (hinj : ∀ (n : ℕ), Function.Injective ⇑(ι n)) (hcover : ∀ (x : L), ∃ n y, (ι n) y = x)
  (hfinal : ∀ (ψ : L →ₗ[𝕜] 𝕜), (∀ (n : ℕ), Continuous (⇑ψ ∘ ⇑(ι n))) → Continuous ⇑ψ) :
  StrongDual 𝕜 L ≃L[𝕜] ↥(TauCeti.dualProjectiveLimit T)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Gantmacher's criterion](../../../part-01/analysis/part-03/normed/part-01/gantmachers-criterion.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.dualProjectiveLimit.strongDualEquiv`](https://taucetiproject.org/docs/TauCeti/Analysis/LocallyConvex/CompactInductiveLimit.html#TauCeti.dualProjectiveLimit.strongDualEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.dualProjectiveLimit.strongDualEquiv`](https://taucetiproject.org/docs/TauCeti/Analysis/LocallyConvex/CompactInductiveLimit.html#TauCeti.dualProjectiveLimit.strongDualEquiv)
- [Source of `TauCeti.dualProjectiveLimit.strongDualEquiv` in TauCeti/Analysis/LocallyConvex/CompactInductiveLimit.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/LocallyConvex/CompactInductiveLimit.lean#L133)
- [Tau Ceti roadmap status: Sato hyperfunctions and analytic generalized functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Hyperfunctions/STATUS.md)
