---
declaration: theorem
origin: cited
lean: TauCeti.harmonicOnNhd_iSup_of_monotone
statement: formalized
proof: formalized
---

# The limit in Harnack's convergence theorem is harmonic

Let `F` be a family of functions
harmonic on a preconnected open set `U`, monotone at each point of `U` and bounded above at some
point `x₀ ∈ U`. Then its pointwise supremum is harmonic on `U`.

```lean
TauCeti.harmonicOnNhd_iSup_of_monotone.{u_1, u_2} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {ι : Type u_2} [SemilatticeSup ι] [Nonempty ι]
  {F : ι → E → ℝ} {U : Set E} (hU : IsOpen U) (hUc : IsPreconnected U)
  (hF : ∀ (i : ι), InnerProductSpace.HarmonicOnNhd (F i) U)
  (hmono : ∀ x ∈ U, Monotone fun i => F i x) {x₀ : E} (hx₀ : x₀ ∈ U)
  (hbdd : BddAbove (Set.range fun i => F i x₀)) :
  InnerProductSpace.HarmonicOnNhd (fun x => ⨆ i, F i x) U
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The du Bois-Reymond lemma](../../../part-01/integral-currents-geometric-homology-and-minimiz/the-du-bois-reymond-lemma.md)
- [Green's second identity against a test function](../../sobolev/part-01/greens-second-identity-against-a-test-function.md)
- [Harnack's convergence theorem](harnacks-convergence-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.harmonicOnNhd_iSup_of_monotone`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Harnack/Convergence.html#TauCeti.harmonicOnNhd_iSup_of_monotone).

## Sources

- [Tau Ceti documentation: `TauCeti.harmonicOnNhd_iSup_of_monotone`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Harnack/Convergence.html#TauCeti.harmonicOnNhd_iSup_of_monotone)
- [Source of `TauCeti.harmonicOnNhd_iSup_of_monotone` in TauCeti/Analysis/PDE/Harnack/Convergence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Harnack/Convergence.lean#L87)
