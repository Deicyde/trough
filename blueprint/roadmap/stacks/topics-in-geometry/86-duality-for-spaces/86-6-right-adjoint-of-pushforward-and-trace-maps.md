---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.quasicoherentDerivedRightAdjointBaseChangeMap_trace, AlgebraicGeometry.Space.quasicoherentDerivedRightAdjointBaseChangeMap_unit
statement: formalized
proof: formalized
---

# 86.6 Right adjoint of pushforward and trace maps

Section 86.6 of the Stacks Project, [Tag 0E5K](https://stacks.math.columbia.edu/tag/0E5K). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E5L, a lemma

[Tag 0E5L](https://stacks.math.columbia.edu/tag/0E5L) in the Stacks Project.

**`AlgebraicGeometry.Space.quasicoherentDerivedRightAdjointBaseChangeMap_trace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityBaseChangeMap.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityBaseChangeMap.lean#L148).

> **Stacks 0E5L.**  The trace maps and the base change maps agree: `Lg^*` of the trace
> `Rf_* a K ⟶ K` is the base change map `β` at `a K`, followed by `Rf'_*` of the map `α` of
> Stacks 0E5D and the trace `Rf'_* a' (Lg^* K) ⟶ Lg^* K`.

```lean
theorem quasicoherentDerivedRightAdjointBaseChangeMap_trace (K) :
    (squareBaseChange hZ sq hXqc hXqs hYqs hY'qc hY'qs).app
          ((quasicoherentDerivedRightAdjoint hZ f hXqc hXqs hYqs).obj K) ≫
        (quasicoherentDerivedPushforward B S hS f'
          (isQuasiCompact_of_isQuasiCompactSpace B S hS hZ Y'.2 hY'qs
            (isQuasiCompactSpace_of_isPullback hZ sq hXqc hYqs hY'qc) f'.hom)
          (isQuasiSeparated_of_isAbsolutelyQuasiSeparated_source B S hS hZ X'.2
            (isAbsolutelyQuasiSeparated_of_isPullback hZ sq hXqs hY'qs) f'.hom)).map
          ((quasicoherentDerivedRightAdjointBaseChangeMap hZ sq hXqc hXqs hYqs hY'qc hY'qs
            hTor).app K) ≫
        (squareAdjF' hZ sq hXqc hXqs hYqs hY'qc hY'qs).counit.app
          ((quasicoherentDerivedModulePullback g).obj K) =
      (quasicoherentDerivedModulePullback g).map
        ((squareAdjF hZ hXqc hXqs hYqs).counit.app K)
```

## Tag 0E5M, a lemma

[Tag 0E5M](https://stacks.math.columbia.edu/tag/0E5M) in the Stacks Project.

**`AlgebraicGeometry.Space.quasicoherentDerivedRightAdjointBaseChangeMap_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityBaseChangeMap.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualityBaseChangeMap.lean#L170).

> **Stacks 0E5M.**  The units and the base change maps agree: `L(g')^*` of the unit
> `K ⟶ a (Rf_* K)`, followed by the map `α` of Stacks 0E5D at `Rf_* K` and by `a'` of the base
> change map `β`, is the unit `L(g')^* K ⟶ a' (Rf'_* L(g')^* K)`.

```lean
theorem quasicoherentDerivedRightAdjointBaseChangeMap_unit (K) :
    (quasicoherentDerivedModulePullback g').map ((squareAdjF hZ hXqc hXqs hYqs).unit.app K) ≫
        (quasicoherentDerivedRightAdjointBaseChangeMap hZ sq hXqc hXqs hYqs hY'qc hY'qs
          hTor).app ((quasicoherentDerivedPushforward B S hS f
            (isQuasiCompact_of_isQuasiCompactSpace B S hS hZ Y.2 hYqs hXqc f.hom)
            (isQuasiSeparated_of_isAbsolutelyQuasiSeparated_source B S hS hZ X.2 hXqs
              f.hom)).obj K) ≫
        (quasicoherentDerivedRightAdjoint hZ f'
          (isQuasiCompactSpace_of_isPullback hZ sq hXqc hYqs hY'qc)
          (isAbsolutelyQuasiSeparated_of_isPullback hZ sq hXqs hY'qs) hY'qs).map
          ((squareBaseChange hZ sq hXqc hXqs hYqs hY'qc hY'qs).app K) =
      (squareAdjF' hZ sq hXqc hXqs hYqs hY'qc hY'qs).unit.app
        ((quasicoherentDerivedModulePullback g').obj K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 86.6, Tag 0E5K](https://stacks.math.columbia.edu/tag/0E5K)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
