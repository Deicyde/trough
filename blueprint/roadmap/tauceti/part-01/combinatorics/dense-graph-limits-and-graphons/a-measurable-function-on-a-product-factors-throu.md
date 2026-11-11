---
declaration: theorem
origin: cited
lean: Measurable.exists_eq_measurable_comp_prodMap
statement: formalized
proof: formalized
---

# A measurable function on a product factors through Boolean coordinates

A measurable
`f : α × β → γ` into a nonempty standard Borel space is a measurable function of countably many
Boolean coordinates of each argument: no hypothesis on `α` or `β` is needed, which is what lets a
kernel on an arbitrary carrier be transported to a standard Borel one.

```lean
Measurable.exists_eq_measurable_comp_prodMap.{u_1, u_2, u_3} {α : Type u_1} {β : Type u_2}
  {γ : Type u_3} [MeasurableSpace α] [MeasurableSpace β] [MeasurableSpace γ] [StandardBorelSpace γ]
  [Nonempty γ] {f : α × β → γ} (hf : Measurable f) :
  ∃ q r g, Measurable q ∧ Measurable r ∧ Measurable g ∧ f = g ∘ Prod.map q r
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Measurable.exists_eq_measurable_comp_prodMap`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/MeasurableSpace/CountablyGenerated.html#Measurable.exists_eq_measurable_comp_prodMap).

## Sources

- [Tau Ceti documentation: `Measurable.exists_eq_measurable_comp_prodMap`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/MeasurableSpace/CountablyGenerated.html#Measurable.exists_eq_measurable_comp_prodMap)
- [Source of `Measurable.exists_eq_measurable_comp_prodMap` in TauCeti/MeasureTheory/MeasurableSpace/CountablyGenerated.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/MeasurableSpace/CountablyGenerated.lean#L136)
- [Tau Ceti roadmap status: Dense graph limits and graphons](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/DenseGraphLimits/STATUS.md)
