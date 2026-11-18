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

- [The du Bois-Reymond lemma](../../../part-03/distribution/the-du-bois-reymond-lemma.md)
- [Green's second identity against a test function](../../sobolev/part-01/greens-second-identity-against-a-test-function.md)
- [Hopf's boundary-point lemma (`TauCeti.fderiv_pos_of_laplacian_nonneg_of_lt_ball_of_le_sphere`)](../../../part-03/inner-product-space/part-01/hopfs-boundary-point-lemma-tauceti-fderiv-pos-of.md)
- [The limit in Harnack's convergence theorem is harmonic](../part-02/the-limit-in-harnacks-convergence-theorem-is-har.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.harmonicOnNhd_perronSolution`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Perron/Basic.html#TauCeti.harmonicOnNhd_perronSolution).

## Sources

- [Tau Ceti documentation: `TauCeti.harmonicOnNhd_perronSolution`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Perron/Basic.html#TauCeti.harmonicOnNhd_perronSolution)
- [Source of `TauCeti.harmonicOnNhd_perronSolution` in TauCeti/Analysis/PDE/Perron/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Perron/Basic.lean#L357)
