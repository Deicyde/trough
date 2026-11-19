---
declaration: theorem
origin: cited
lean: FirstOrder.Language.wellOrdering_undefinable
statement: formalized
proof: formalized
---

# Undefinability of well-ordering

Among countable nonempty structures in `Type w`, no
`L_{ω₁ω}` sentence holds in a structure if and only if `lt` is a well-order. A fortiori no
sentence has as its models exactly the structures in `Type w` in which `lt` is a well-order, which
is the statement in Marker, §4.4.

```lean
FirstOrder.Language.wellOrdering_undefinable.{u, v, w} {L : FirstOrder.Language}
  (lt : L.Relations 2) :
  ¬∃ φ,
      ∀ (M : Type w) (x : L.Structure M),
        Nonempty M →
          Countable M →
            (FirstOrder.Language.SentenceInf.Realize φ M ↔
              IsWellOrder M fun x_1 y => FirstOrder.Language.Structure.RelMap lt ![x_1, y])
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)

## Proof depends on

- [Model existence](model-existence.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.wellOrdering_undefinable`](https://taucetiproject.org/docs/TauCeti/ModelTheory/WellOrdering.html#FirstOrder.Language.wellOrdering_undefinable).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.wellOrdering_undefinable`](https://taucetiproject.org/docs/TauCeti/ModelTheory/WellOrdering.html#FirstOrder.Language.wellOrdering_undefinable)
- [Source of `FirstOrder.Language.wellOrdering_undefinable` in TauCeti/ModelTheory/WellOrdering.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/WellOrdering.lean#L726)
- [Tau Ceti roadmap status: Infinitary model existence, omitting types and interpolation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/InfinitaryModelExistence/STATUS.md)
