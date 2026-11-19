---
declaration: theorem
origin: cited
lean: Compile.Batch.Disc.WorldB.setup, VerifiableInference.soundAndBinding, VerifiableInference.completeOnCanServe, VerifiableInference.zeroKnowledgeOnCanServe, VerifiableInference.refusedHandsOutNoProof, VerifiableInference.repliesFit, VerifiableInference.completeAtWellFormedRequests, VerifiableInference.zeroKnowledgeAtEveryRequest
statement: formalized
---

# FlashProve

[anthropics/FlashProve](https://github.com/anthropics/FlashProve) at commit [9e2bdd8f](https://github.com/anthropics/FlashProve/tree/9e2bdd8ff5bf9c62f18263d7dac189b0400b260c), 2026-10-30.

> Version 0.16.0 · A research artifact: not maintained, not accepting contributions.

*Quoted from [README.md](https://github.com/anthropics/FlashProve/blob/9e2bdd8ff5bf9c62f18263d7dac189b0400b260c/README.md), Apache-2.0.*

## Depends on

Its headline statements name no Mathlib concept or declaration mapped elsewhere on this site.

## Proof depends on

- [Discrete law](../../../probability-theory/random-variables-and-their-laws/discrete-law.md)
- [Characteristic p](../../../general-algebra/field-theory/characteristic-p.md)
- [Field](../../../general-algebra/field-theory/field.md)
- [Order of an element](../../../../undergraduate/group-theory/basic-definitions/order-of-an-element.md)
- [Lagrange interpolation](../../../../undergraduate/numerical-analysis/approximation-of-numerical-functions/lagrange-interpolation.md)
- [List](../../list-like-structures/list.md)
- [Associative algebra over a commutative ring](../../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)

## Main results

Its Lean names are 8 of the 11 theorems its README names in code:

- [`Compile.Batch.Disc.WorldB.setup`](https://github.com/anthropics/FlashProve/blob/9e2bdd8ff5bf9c62f18263d7dac189b0400b260c/lean/Compile/Batch/WithinVCB.lean#L130) (theorem)
- [`VerifiableInference.soundAndBinding`](https://github.com/anthropics/FlashProve/blob/9e2bdd8ff5bf9c62f18263d7dac189b0400b260c/lean/AtFullSide/Face/TheSixLines.lean#L99) (theorem)
- [`VerifiableInference.completeOnCanServe`](https://github.com/anthropics/FlashProve/blob/9e2bdd8ff5bf9c62f18263d7dac189b0400b260c/lean/AtFullSide/Face/TheSixLines.lean#L106) (theorem)
- [`VerifiableInference.zeroKnowledgeOnCanServe`](https://github.com/anthropics/FlashProve/blob/9e2bdd8ff5bf9c62f18263d7dac189b0400b260c/lean/AtFullSide/Face/TheSixLines.lean#L122) (theorem)
- [`VerifiableInference.refusedHandsOutNoProof`](https://github.com/anthropics/FlashProve/blob/9e2bdd8ff5bf9c62f18263d7dac189b0400b260c/lean/AtFullSide/Face/TheSixLines.lean#L134) (theorem)
- [`VerifiableInference.repliesFit`](https://github.com/anthropics/FlashProve/blob/9e2bdd8ff5bf9c62f18263d7dac189b0400b260c/lean/AtFullSide/Face/TheSixLines.lean#L144) (theorem)
- [`VerifiableInference.completeAtWellFormedRequests`](https://github.com/anthropics/FlashProve/blob/9e2bdd8ff5bf9c62f18263d7dac189b0400b260c/lean/AtFullSide/Face/TheSixLines.lean#L173) (theorem)
- [`VerifiableInference.zeroKnowledgeAtEveryRequest`](https://github.com/anthropics/FlashProve/blob/9e2bdd8ff5bf9c62f18263d7dac189b0400b260c/lean/AtFullSide/Face/TheSixLines.lean#L235) (theorem)

Of the files its headlines import, directly or not, `lean/E2E/KeyListed.lean` hold `sorry` or `admit`.

## Project

- Lean v4.29.1, Mathlib at [5e932f97](https://github.com/leanprover-community/mathlib4/tree/5e932f97dd25535344f80f9dd8da3aab83df0fe6).
- 29,566 .lean files; its Lean libraries `Library`, `AtFullSide`, `ShapeLines` hold 5,000 (the first read), declaring 60,697 names, with `sorry` in 4 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/anthropics/FlashProve/blob/9e2bdd8ff5bf9c62f18263d7dac189b0400b260c/LICENSE)).

## Builds on

- Mathlib, at [5e932f97](https://github.com/leanprover-community/mathlib4/tree/5e932f97dd25535344f80f9dd8da3aab83df0fe6).

## Placement

Of its imports of Mathlib modules in an overview area, 84 of 314 are in Data structures, 1.9 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (84 of 314 imports, 1.9×), Linear algebra (34 of 314 imports, 1.9×), General algebra (146 of 314 imports, 1.3×). *Proof depends on* lists 8 of the 36 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [anthropics/FlashProve at 9e2bdd8f](https://github.com/anthropics/FlashProve/tree/9e2bdd8ff5bf9c62f18263d7dac189b0400b260c)
