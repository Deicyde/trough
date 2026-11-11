---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.Modules.isSheaf_bigPresheaf_fpqcTopology
statement: formalized
proof: formalized
---

# fpqc descent of sections of quasi-coherent modules

For a quasi-coherent `𝒪_S`-module `F`,
the presheaf `(T, h) ↦ Γ(T, h^* F)` underlying `bigPresheaf F` is a sheaf for the fpqc topology on
the big site `Over S` (Stacks, Lemma 35.8.1).

```lean
AlgebraicGeometry.Scheme.Modules.isSheaf_bigPresheaf_fpqcTopology.{u} {S : AlgebraicGeometry.Scheme}
  (F : S.Modules) [SheafOfModules.IsQuasicoherent F] :
  CategoryTheory.Presheaf.IsSheaf (AlgebraicGeometry.Scheme.fpqcTopology.over S)
    F.bigPresheaf.presheaf
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.Modules.isSheaf_bigPresheaf_fpqcTopology`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Sites/Big/Sheaf.html#AlgebraicGeometry.Scheme.Modules.isSheaf_bigPresheaf_fpqcTopology).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.Modules.isSheaf_bigPresheaf_fpqcTopology`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Sites/Big/Sheaf.html#AlgebraicGeometry.Scheme.Modules.isSheaf_bigPresheaf_fpqcTopology)
- [Source of `AlgebraicGeometry.Scheme.Modules.isSheaf_bigPresheaf_fpqcTopology` in TauCeti/AlgebraicGeometry/Sites/Big/Sheaf.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Sites/Big/Sheaf.lean#L118)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
