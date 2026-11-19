---
declaration: theorem
origin: cited
lean: TauCeti.Vortex.framedVortexDivisor_surjective
statement: formalized
proof: formalized
---

# Taubes's existence theorem

Every effective divisor of degree `m` is the divisor of a
smooth framed degree-`m` vortex.

```lean
TauCeti.Vortex.framedVortexDivisor_surjective (m : ℕ) :
  Function.Surjective TauCeti.Vortex.framedVortexDivisor
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The borderline Sobolev inequality on `W^{1,n}_0(Ω)`](../../part-04/sobolev/part-01/the-borderline-sobolev-inequality-on-w-1-n-0.md)
- [The Cauchy–Pompeiu formula with a cutoff](../../part-03/complex/part-01/the-cauchy-pompeiu-formula-with-a-cutoff.md)
- [The Cauchy–Schwarz inequality](../../../measure-theory/integral/part-01/the-cauchy-schwarz-inequality.md)
- [De Giorgi's theorem up to a flat boundary](../partial-differential-equations/de-giorgis-theorem-up-to-a-flat-boundary.md)
- [The Gagliardo–Nirenberg–Sobolev inequality in dimension two](../../part-04/sobolev/part-01/the-gagliardo-nirenberg-sobolev-inequality-in-di.md)
- [Green's second identity against a test function](../../part-04/sobolev/part-01/greens-second-identity-against-a-test-function.md)
- [Hölder's bound on an average](../../../measure-theory/integral/part-02/holders-bound-on-an-average.md)
- [Hölder's inequality for disjoint pieces](../../../measure-theory/function/part-01/holders-inequality-for-disjoint-pieces.md)
- [Interior Schauder estimate at positive times](../../part-04/pde/part-02/interior-schauder-estimate-at-positive-times.md)
- [Meyers–Serrin: `H = W` in `W^{k,p}(Ω)`](../../part-04/sobolev/part-02/meyers-serrin-h-w-in-w-k-p.md)
- [Milman–Pettis theorem](../../part-03/convex/milman-pettis-theorem.md)
- [The monotone du Bois-Reymond lemma](../../part-03/distribution/the-monotone-du-bois-reymond-lemma.md)
- [Rademacher's theorem for locally Lipschitz functions](../../part-03/calculus/part-02/rademachers-theorem-for-locally-lipschitz-functi.md)
- [Radial fundamental theorem of calculus](../../../measure-theory/constructions/radial-fundamental-theorem-of-calculus.md)
- [Trudinger's inequality on `W^{1,n}_0(Ω)`](../../part-04/sobolev/part-02/trudingers-inequality-on-w-1-n-0.md)
- [Weyl's lemma for continuous functions](../../part-03/inner-product-space/part-03/weyls-lemma-for-continuous-functions.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Vortex.framedVortexDivisor_surjective`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/Existence.html#TauCeti.Vortex.framedVortexDivisor_surjective).

## Sources

- [Tau Ceti documentation: `TauCeti.Vortex.framedVortexDivisor_surjective`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/Existence.html#TauCeti.Vortex.framedVortexDivisor_surjective)
- [Source of `TauCeti.Vortex.framedVortexDivisor_surjective` in TauCeti/Analysis/PDE/Vortex/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Vortex/Existence.lean#L310)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TaubesGromov/STATUS.md)
