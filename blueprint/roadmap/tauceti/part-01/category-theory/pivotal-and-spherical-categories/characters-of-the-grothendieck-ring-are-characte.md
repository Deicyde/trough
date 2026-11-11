---
declaration: theorem
origin: cited
lean: TauCeti.SplitK0.ringHom_apply_dual
statement: formalized
proof: formalized
---

# Characters of the Grothendieck ring are ⋆-characters

A ring homomorphism `ψ` from the
Grothendieck ring of a fusion category to `ℝ` or `ℂ` intertwines the duality `[X] ↦ [Xᘁ]` with
complex conjugation.

```lean
TauCeti.SplitK0.ringHom_apply_dual.{w, w', v, u, u_1} (k : Type w') [Field k] [IsAlgClosed k]
  {C : Type u} [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.MonoidalPreadditive C]
  [CategoryTheory.RigidCategory C] [CategoryTheory.Linear k C] [CategoryTheory.MonoidalLinear k C]
  [TauCeti.IsFiniteSemisimpleCategory C] [∀ (X Y : C), FiniteDimensional k (X ⟶ Y)]
  [CategoryTheory.EssentiallySmall.{w, v, u} C] [Finite (TauCeti.SimpleClasses C)] {𝕜 : Type u_1}
  [RCLike 𝕜] (ψ : TauCeti.SplitK0 C →+* 𝕜) (x : TauCeti.SplitK0 C) :
  ψ (TauCeti.SplitK0.dual x) = (starRingEnd 𝕜) (ψ x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Frobenius reciprocity in multiplicity form](../other-results/frobenius-reciprocity-in-multiplicity-form.md)
- [TauCeti.fusionCoeff](tauceti-fusioncoeff.md)
- [TauCeti.SplitK0.simpleBasis](tauceti-splitk0-simplebasis.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SplitK0.ringHom_apply_dual`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Semisimple/Character.html#TauCeti.SplitK0.ringHom_apply_dual).

## Sources

- [Tau Ceti documentation: `TauCeti.SplitK0.ringHom_apply_dual`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Semisimple/Character.html#TauCeti.SplitK0.ringHom_apply_dual)
- [Source of `TauCeti.SplitK0.ringHom_apply_dual` in TauCeti/CategoryTheory/Semisimple/Character.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Semisimple/Character.lean#L105)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PivotalSpherical/STATUS.md)
