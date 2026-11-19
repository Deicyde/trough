---
declaration: theorem
origin: cited
lean: TauCeti.ValidLieTypeIndex.isSimpleGroup_A
statement: formalized
proof: formalized
---

# Every `A_r(q)` on the classification list is simple

On the constructor `A r q` the
Steinberg endomorphism of the assembly is that of the type-`A` family, so the assembled candidate
is the type-`A` one.

```lean
TauCeti.ValidLieTypeIndex.isSimpleGroup_A {r : ℕ} {q : TauCeti.PrimePower}
  (hv : (TauCeti.LieTypeIndex.A r q).Valid) :
  IsSimpleGroup (TauCeti.ValidLieTypeIndex.Group ⟨TauCeti.LieTypeIndex.A r q, hv⟩)
```

## Depends on

- [The ambient group of a valid Lie-type index](../stating-the-classification-of-finite-simple-grou/the-ambient-group-of-a-valid-lie-type-index.md)
- [TauCeti.ValidLieTypeIndex.Group](../stating-the-classification-of-finite-simple-grou/tauceti-validlietypeindex-group.md)

## Proof depends on

- [Cauchy--Binet for `2 × 2` minors](../../linear-algebra/part-01/matrix/cauchy-binet-for-2-2-minors.md)
- [Iwasawa's theorem for `PSL`](iwasawas-theorem-for-psl.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ValidLieTypeIndex.isSimpleGroup_A`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/TypeA.html#TauCeti.ValidLieTypeIndex.isSimpleGroup_A).

## Sources

- [Tau Ceti documentation: `TauCeti.ValidLieTypeIndex.isSimpleGroup_A`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/TypeA.html#TauCeti.ValidLieTypeIndex.isSimpleGroup_A)
- [Source of `TauCeti.ValidLieTypeIndex.isSimpleGroup_A` in TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/TypeA.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/TypeA.lean#L188)
- [Tau Ceti roadmap status: Finiteness and simplicity of the groups on the CFSG list](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CFSGBasicProperties/STATUS.md)
