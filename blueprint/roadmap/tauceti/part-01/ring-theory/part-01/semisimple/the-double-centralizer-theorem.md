---
declaration: theorem
origin: cited
lean: TauCeti.toModuleEnd_moduleEnd_bijective, TauCeti.algEquivEndEndOfIsSimpleRing, TauCeti.toModuleEnd_moduleEnd_bijective_of_isSimpleRing, AlgHom.centralizer_centralizer_range, Subalgebra.centralizer_centralizer_of_isSemisimpleModule
statement: formalized
proof: formalized
---

# The double centralizer theorem

Let `M` be a faithful semisimple `R`-module which is finite
over its endomorphism ring `D = Module.End R M`. Then the natural map `R → Module.End D M` is
bijective: `R` is exactly the ring of `D`-linear endomorphisms of `M`.

This sharpens Mathlib's `Module.Finite.toModuleEnd_moduleEnd_surjective` from surjectivity to
bijectivity; the extra input is faithfulness, which is what makes the map injective.

```lean
TauCeti.toModuleEnd_moduleEnd_bijective.{u_1, u_2} (R : Type u_1) [Ring R] (M : Type u_2)
  [AddCommGroup M] [_root_.Module R M] [IsSemisimpleModule R M] [FaithfulSMul R M]
  [Module.Finite (Module.End R M) M] : Function.Bijective ⇑(Module.toModuleEnd (Module.End R M) M)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.toModuleEnd_moduleEnd_bijective`](https://taucetiproject.org/docs/TauCeti/RingTheory/Semisimple/DoubleCentralizer.html#TauCeti.toModuleEnd_moduleEnd_bijective).

## Other forms

**The double centralizer theorem for a finite module over a simple algebra.** Formalized in Tau Ceti as [`TauCeti.algEquivEndEndOfIsSimpleRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Semisimple/DoubleCentralizer.html#TauCeti.algEquivEndEndOfIsSimpleRing).

```lean
TauCeti.algEquivEndEndOfIsSimpleRing.{u_1, u_2, u_3} (R : Type u_1) [Ring R] (M : Type u_2)
  [AddCommGroup M] [_root_.Module R M] (K : Type u_3) [CommSemiring K] [Algebra K R]
  [_root_.Module K M] [IsScalarTower K R M] [Module.Finite K M] [IsSimpleRing R]
  [IsSemisimpleModule R M] [Nontrivial M] : R ≃ₐ[K] Module.End (Module.End R M) M
```

**The double centralizer theorem for a simple ring.** Formalized in Tau Ceti as [`TauCeti.toModuleEnd_moduleEnd_bijective_of_isSimpleRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Semisimple/DoubleCentralizer.html#TauCeti.toModuleEnd_moduleEnd_bijective_of_isSimpleRing).

```lean
TauCeti.toModuleEnd_moduleEnd_bijective_of_isSimpleRing.{u_1, u_2} (R : Type u_1) [Ring R]
  (M : Type u_2) [AddCommGroup M] [_root_.Module R M] [IsSimpleRing R] [IsSemisimpleModule R M]
  [Nontrivial M] [Module.Finite (Module.End R M) M] :
  Function.Bijective ⇑(Module.toModuleEnd (Module.End R M) M)
```

**The double centralizer theorem for the image of a semisimple algebra.** Formalized in Tau Ceti as [`AlgHom.centralizer_centralizer_range`](https://taucetiproject.org/docs/TauCeti/RingTheory/Semisimple/DoubleCentralizer.html#AlgHom.centralizer_centralizer_range).

```lean
AlgHom.centralizer_centralizer_range.{u_3, u_4, u_5} {K : Type u_3} [CommRing K] {N : Type u_4}
  [AddCommGroup N] [_root_.Module K N] {S : Type u_5} [Ring S] [Algebra K S] [IsSemisimpleRing S]
  (ρ : S →ₐ[K] Module.End K N) [Module.Finite (Module.End (↥ρ.range) N) N] :
  Subalgebra.centralizer K ↑(Subalgebra.centralizer K ↑ρ.range) = ρ.range
```

**The double centralizer theorem inside an endomorphism algebra.** Formalized in Tau Ceti as [`Subalgebra.centralizer_centralizer_of_isSemisimpleModule`](https://taucetiproject.org/docs/TauCeti/RingTheory/Semisimple/DoubleCentralizer.html#Subalgebra.centralizer_centralizer_of_isSemisimpleModule).

```lean
Subalgebra.centralizer_centralizer_of_isSemisimpleModule.{u_3, u_4} {K : Type u_3} [CommRing K]
  {N : Type u_4} [AddCommGroup N] [_root_.Module K N] (A : Subalgebra K (Module.End K N))
  [Module.Finite (Module.End (↥A) N) N] [IsSemisimpleModule (↥A) N] :
  Subalgebra.centralizer K ↑(Subalgebra.centralizer K ↑A) = A
```

## Sources

- [Tau Ceti documentation: `TauCeti.toModuleEnd_moduleEnd_bijective`](https://taucetiproject.org/docs/TauCeti/RingTheory/Semisimple/DoubleCentralizer.html#TauCeti.toModuleEnd_moduleEnd_bijective)
- [Source of `TauCeti.toModuleEnd_moduleEnd_bijective` in TauCeti/RingTheory/Semisimple/DoubleCentralizer.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Semisimple/DoubleCentralizer.lean#L112)
