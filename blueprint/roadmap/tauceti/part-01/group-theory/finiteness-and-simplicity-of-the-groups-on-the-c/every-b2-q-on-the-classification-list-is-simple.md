---
declaration: theorem
origin: cited
lean: TauCeti.ValidLieTypeIndex.isSimpleGroup_B_two
statement: formalized
proof: formalized
---

# Every `B₂(q)` on the classification list is simple

On the constructor `B 2 q` the
Steinberg endomorphism of the assembly is that of the type-`B` family, so the assembled candidate
is the one of `TauCeti.TypeB2LieIndex.of q hv`.

```lean
TauCeti.ValidLieTypeIndex.isSimpleGroup_B_two {q : TauCeti.PrimePower}
  (hv : (TauCeti.LieTypeIndex.B 2 q).Valid) :
  IsSimpleGroup (TauCeti.ValidLieTypeIndex.Group ⟨TauCeti.LieTypeIndex.B 2 q, hv⟩)
```

## Depends on

- [The ambient group of a valid Lie-type index](../stating-the-classification-of-finite-simple-grou/the-ambient-group-of-a-valid-lie-type-index.md)
- [TauCeti.ValidLieTypeIndex.Group](../stating-the-classification-of-finite-simple-grou/tauceti-validlietypeindex-group.md)

## Proof depends on

- [Cauchy--Binet for `2 × 2` minors](../../linear-algebra/matrix/cauchy-binet-for-2-2-minors.md)
- [Iwasawa's theorem for the projective symplectic group](../../linear-algebra/matrix/iwasawas-theorem-for-the-projective-symplectic-g.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ValidLieTypeIndex.isSimpleGroup_B_two`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/TypeB/Two.html#TauCeti.ValidLieTypeIndex.isSimpleGroup_B_two).

## Sources

- [Tau Ceti documentation: `TauCeti.ValidLieTypeIndex.isSimpleGroup_B_two`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/TypeB/Two.html#TauCeti.ValidLieTypeIndex.isSimpleGroup_B_two)
- [Source of `TauCeti.ValidLieTypeIndex.isSimpleGroup_B_two` in TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/TypeB/Two.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/TypeB/Two.lean#L158)
- [Tau Ceti roadmap status: Finiteness and simplicity of the groups on the CFSG list](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CFSGBasicProperties/STATUS.md)
