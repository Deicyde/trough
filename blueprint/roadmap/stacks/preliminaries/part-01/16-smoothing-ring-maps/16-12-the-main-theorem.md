---
declaration: section
origin: cited
lean: Stacks.Smoothing.indSmooth_of_isRegularRingMap
statement: formalized
proof: formalized
---

# 16.12 The main theorem

Section 16.12 of the Stacks Project, [Tag 07GB](https://stacks.math.columbia.edu/tag/07GB). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07GC, a theorem

[Tag 07GC](https://stacks.math.columbia.edu/tag/07GC) in the Stacks Project.

**`Stacks.Smoothing.indSmooth_of_isRegularRingMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/PopescuTheorem.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/PopescuTheorem.lean#L204). The attribute's comment: “Popescu's theorem with NO carried hypotheses: every regular ring map of Noetherian rings is a filtered colimit of smooth ring maps. Regularity is `IsRegularRingMap` (Situation 07F2) and the conclusion is `IndSmooth`, the `ObjectProperty.ind` spelling of Lemma 07C3. Every step of the source's argument is proved: the reduction to a field base (07F5), the Noetherian induction on `𝔥_A`, the case `𝔥_A = Λ` (07EU), the characteristic-zero resolution (07FE), and the characteristic-`p` resolution (07FJ, `canBeResolvedInPositiveCharacteristic`), whose own λ-choice repair is due to Brian Nugent. Nothing is assumed.”.

> **Popescu's theorem.** A regular ring map of Noetherian rings makes its target a filtered
> colimit of smooth algebras.

```lean
theorem indSmooth_of_isRegularRingMap
    (R : Type u) [CommRing R] (Λ : Type u) [CommRing Λ] [Algebra R Λ]
    [IsNoetherianRing R] [IsNoetherianRing Λ] (hregular : IsRegularRingMap R Λ) :
    IndSmooth R Λ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 16.12, Tag 07GB](https://stacks.math.columbia.edu/tag/07GB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
