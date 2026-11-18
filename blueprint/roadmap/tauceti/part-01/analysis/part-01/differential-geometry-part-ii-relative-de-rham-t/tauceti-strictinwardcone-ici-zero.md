---
declaration: theorem
origin: cited
lean: TauCeti.strictInwardCone_Ici_zero
statement: formalized
proof: formalized
---

# TauCeti.strictInwardCone_Ici_zero

At the endpoint of the half-line the strict cone is the positive, not the nonnegative,
half-line. In particular neither zero nor an outward vector is admitted.

```lean
TauCeti.strictInwardCone_Ici_zero : TauCeti.strictInwardCone (Set.Ici 0) 0 = Set.Ioi 0
```

## Depends on

- [TauCeti.strictInwardCone](tauceti-strictinwardcone.md)

## Proof depends on

- [Convex.mem_strictInwardCone_iff](convex-mem-strictinwardcone-iff.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.strictInwardCone_Ici_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Cone/StrictInward.html#TauCeti.strictInwardCone_Ici_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.strictInwardCone_Ici_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Cone/StrictInward.html#TauCeti.strictInwardCone_Ici_zero)
- [Source of `TauCeti.strictInwardCone_Ici_zero` in TauCeti/Analysis/Convex/Cone/StrictInward.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Convex/Cone/StrictInward.lean#L327)
- [Tau Ceti roadmap status: Differential geometry, Part II — relative de Rham theory, fundamental classes and relative transversality](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DeRhamCohomologyAndDuality/STATUS.md)
