---
declaration: theorem
origin: cited
lean: TauCeti.harmonicOnNhd_perronSolution
statement: formalized
proof: formalized
---

# Perron's theorem

Let `Ω` be a bounded open set, let `g` be bounded above on
`frontier Ω`, and suppose the Perron family of `g` is nonempty. Then the Perron solution
`TauCeti.perronSolution Ω g` is harmonic in `Ω`.

In Perron's setting of bounded boundary data the family is nonempty by
`TauCeti.perronFamily_nonempty`.

```lean
TauCeti.harmonicOnNhd_perronSolution.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {Ω : Set E} {g : E → ℝ} [MeasurableSpace E]
  [BorelSpace E] (hΩ : IsOpen Ω) (hb : Bornology.IsBounded Ω) (hg : BddAbove (g '' frontier Ω))
  (hne : (TauCeti.perronFamily Ω g).Nonempty) :
  InnerProductSpace.HarmonicOnNhd (TauCeti.perronSolution Ω g) Ω
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The du Bois-Reymond lemma](../../../part-01/integral-currents-geometric-homology-and-minimiz/the-du-bois-reymond-lemma.md)
- [Green's second identity against a test function](../../sobolev/part-01/greens-second-identity-against-a-test-function.md)
- [Hopf's boundary-point lemma](../../inner-product-space/part-01/hopfs-boundary-point-lemma.md)
- [The limit in Harnack's convergence theorem is harmonic](the-limit-in-harnacks-convergence-theorem-is-har.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.harmonicOnNhd_perronSolution`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Perron/Basic.html#TauCeti.harmonicOnNhd_perronSolution).

## Sources

- [Tau Ceti documentation: `TauCeti.harmonicOnNhd_perronSolution`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Perron/Basic.html#TauCeti.harmonicOnNhd_perronSolution)
- [Source of `TauCeti.harmonicOnNhd_perronSolution` in TauCeti/Analysis/PDE/Perron/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Perron/Basic.lean#L342)
