---
declaration: section
origin: cited
lean: OAI.Thomason.main
statement: formalized
---

# 317. Thomason model structures in all strict higher dimensions

1 manuscript and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the Ara–Maltsiniotis conjecture: for every *n* ≥ 1 and *n* = *ω*, small strict globular *n*-categories admit proper combinatorial Thomason model structures Quillen equivalent to simplicial sets. Thus strict higher categories model the homotopy theory of spaces in every stated dimension.

## Thomason Model Structures in Every Strict Higher Dimension

We prove the higher-dimensional Thomason model-structure conjecture of Ara and Maltsiniotis. For every $1\le n\le\infty$, the category of small strict globular *n*-categories admits a proper combinatorial model structure that is Quillen equivalent to simplicial sets. Its weak equivalences and fibrations are detected by the twice-extended Street nerve $\mathrm{Ex}^2N_n$, and the Quillen equivalence is given by $c_n\mathrm{Sd}^2\dashv\mathrm{Ex}^2N_n$. Thus strict higher categories model the homotopy theory of spaces in every positive finite dimension and in dimension *ω*.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Thomason-Model-Structures-in-Every-Strict-Higher-Dimension-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves the higher-dimensional Thomason model-structure theorem for small strict globular $n$-categories in every positive finite dimension and in dimension $\omega$. Each category has the stated proper combinatorial model structure, Quillen equivalent to simplicial sets through the twice-subdivided categorification and twice-extended Street nerve adjunction.

The selected statements also identify weak equivalences by the Street nerve in all these dimensions. Thus the constructions model the homotopy theory of spaces throughout the stated range.

## Lean: Thomason model structures and nerve detection in all positive strict dimensions

Stated in [ThomasonModelStructures.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ThomasonModelStructures.lean).

```lean
theorem Thomason.main : OAI.Thomason.FullMain.{u}
```

Proved in [lean/OAI/CategoryTheory/Thomason/RankedFaithfulness.lean, line 683](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/CategoryTheory/Thomason/RankedFaithfulness.lean#L683).

```lean
theorem Thomason.nerveDetection_allDimensions :
    OAI.Thomason.thomasonWeakEquivalences.{u} =
      OAI.Thomason.simplicialWeakEquivalences.inverseImage OAI.Thomason.streetNerveFunctor ∧
    ∀ n : ℕ, OAI.Thomason.thomasonWeakEquivalencesFinite.{u} n =
      OAI.Thomason.simplicialWeakEquivalences.inverseImage (OAI.Thomason.streetNerveFinite n)
```

Its proof is in [lean/OAI/CategoryTheory/Thomason/RankedFaithfulness.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/CategoryTheory/Thomason/RankedFaithfulness.lean) or a file it imports further down, which this chapter does not read.

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/317.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/317.md)
