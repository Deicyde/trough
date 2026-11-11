# Classification of Finite Simple Groups (Axiom)

[AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) is a Lean proof of the classification of finite simple groups, by Axiom Math. Its README says:

> A sorry-free Lean4 (v4.35.0-rc3) proof of the Classification of Finite Simple Groups (CFSG), built on Mathlib and TauCeti, using the standard axioms `Classical.choice`, `propext`, and `Quot.sound` (no `native_decide`). We primarily follow the first generation proof of CFSG.
>
> We use the [statement of CFSG from the TauCeti project](https://github.com/TauCetiProject/TauCeti/blob/6e0c6acab5f4c6f42e5f5bab9bd5e4e84f74c380/TauCeti/GroupTheory/SpecificGroups/CFSG/Classification.lean#L52-L56)
>
> ```lean4
> /-- **Classification of finite simple groups, statement only.** Every finite simple group is
> isomorphic to one of the explicitly constructed groups on the classification list. -/
> def ClassificationStatement : Prop :=
>   ∀ (G : Type u) [Group G] [Finite G] [IsSimpleGroup G],
>     ∃ i : CFSGIndex, Nonempty (G ≃* i.Group)
> ```

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG), read at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962) (2026-10-27).
- Lean toolchain v4.35.0-rc3, Mathlib at [b63f6e8a](https://github.com/leanprover-community/mathlib4/tree/b63f6e8a68d220e3b3bc4f3792bb53650d375f24).
- License: Apache-2.0.
- Authors: Dean Cureton, Vasily Ilin, Bhavik Mehta, Niels Voss, Rafael Cabral, Colin Defant, Erik Gregory, Aaron Hill, Letong Hong, Qinheping Hu, Dustin Jamner, Albert Jiang, Tadeusz Jordan, Andranik Kurghinyan, Kenny Lau, Jonathan Laurent, David Liang, Jannis Limperg, Simon Mahns, Brian Nugent, Connor Olson, Ken Ono, Eric Paul, Dhruv Rajan, Karun Ram, Charlie Ray, Ho Chung Siu, Ashvin A. Swaminathan, Jesse Thorner, Aleksey Tsaplin, Chenkai Wang.
- Review status: “self-assessed”.
- Reviewers: “Axiom Math”.
- Automation: autonomous; framework “AxiomProver”
- Tau Ceti at [6e0c6aca](https://github.com/TauCetiProject/TauCeti/tree/6e0c6acab5f4c6f42e5f5bab9bd5e4e84f74c380), a Lake dependency; the README says the proof uses Tau Ceti's statement of the classification.

## Main results

Its formalization.yaml names 2 main results.

`CFSGComparator.classification` (theorem), in [Comparator/Solution.lean, line 10](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/Comparator/Solution.lean#L10). Its statement:

```lean
theorem CFSGComparator.classification : TauCeti.ClassificationStatement.{u}
```

It names `TauCeti.ClassificationStatement`, which has [an article](../tauceti/part-01/group-theory/stating-the-classification-of-finite-simple-grou/classification-of-finite-simple-groups-statement.md) in the Tau Ceti chapter.

`CFSG.Milestones.cfsg_classification_native_and_realization` (theorem), in [CFSG/Milestones/CFSG_classification.lean, line 4633](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CFSG_classification.lean#L4633). Its milestone has [an article](milestones/part-01/cfsg-classification.md).

## This map

The chapter follows the proof as the repository writes it. [`CFSG.classification_finite_simple_groups`](case-division/top-theorem.md), in CFSG/Statement.lean, states the classification. Its proof applies `CFSG.Assembly.classification` to 9 theorems, one for each case of a case division that [CFSG/Assembly/Reduction.lean](case-division/reduction.md) defines; [the case division](case-division/README.md) has an article for each of these. [The milestones](milestones/README.md) are the 110 modules directly under `CFSG/Milestones/`, the results the authors single out: 182 declarations in all. An article shows each declaration's Lean statement, or a definition's whole text, its line in the source and its status.

The commit has 194,212 Lean files besides 34,877 certificate files under `Certificates/` and `CFSG/Certificates/`, which are counted, not read. Its largest folders, by the number of files, with the theorems and lemmas their text declares:

- `CFSG/LocalAnalysis/`: 84,451 files, 650,638 theorems and lemmas
- `CFSG/Quasithin/`: 29,236 files, 238,285 theorems and lemmas
- `CFSG/RankThree/`: 19,538 files, 163,215 theorems and lemmas
- `CFSG/GH74/`: 10,791 files, 71,875 theorems and lemmas
- `CFSG/ClassicalInvolution/`: 10,087 files, 73,361 theorems and lemmas
- `CFSG/HardMathSupport/`: 8,357 files, 60,663 theorems and lemmas
- `CFSG/CGT/`: 3,858 files, 34,449 theorems and lemmas
- `CFSG/LieType/`: 3,375 files, 37,830 theorems and lemmas
- `CFSG/Sporadic/`: 3,356 files, 33,364 theorems and lemmas
- `CFSG/Monster/`: 2,109 files, 28,776 theorems and lemmas
- `CFSG/ThirdParty/`: 2,041 files, 25,726 theorems and lemmas
- `CFSG/LargeExtraspecial/`: 1,956 files, 16,012 theorems and lemmas

Docstrings and module docstrings appear only in 1,938 files, under `CFSG/ThirdParty/`, so the titles here are Lean names: a case's article is titled by its theorem, and a milestone's by its file name.

No Lean is run for this chapter. The repository's README says it builds in under 24 hours only with changes to Lake, so its declarations are read from the source text: a declaration's Lean statement is its text up to the `:=` or `where` that starts its value, and “Proved here.” means that value holds no `sorry`. None does, as the repository's formalization.yaml states.

The top theorem's article lists the reduction and the case theorems under what its proof depends on, as its proof names them. Every other edge comes from imports: an edge from one case or milestone to another means that the first one's Lean file imports the other's, directly or through other files, and imports no other case or milestone file that does; an edge implied by two others is left out. There are 301 such edges, shown as what an article depends on (“Statement uses” on the site). 6 case files import CFSG/Assembly/InCatalog.lean, directly or through other files, for the catalog it declares beside the theorem for the case `hab : AbelianStatement`; imports of that file are not edges. An import makes the other file's results available; it does not say which of them a proof uses.

Where a statement writes out the full name of a declaration that has an article in the Tau Ceti chapter, the page that shows the statement links that article: 1 main result above does so.

The README text and Lean source are quoted from [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), under its Apache-2.0 license.

- [The case division](case-division/README.md)
- [Milestones](milestones/README.md)
