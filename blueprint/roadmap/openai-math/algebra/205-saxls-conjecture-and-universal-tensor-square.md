---
declaration: section
origin: cited
lean: OAI.UniversalTensorSquares.universal_tensor_square, OAI.Saxl.saxl_conjecture
statement: formalized
proof: formalized
---

# 205. Saxl’s conjecture and universal tensor squares

2 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves Saxl's conjecture: the tensor square of every staircase representation contains every irreducible complex representation of the corresponding symmetric group. More generally, every $S_{n}$ with $n\notin\{2,4,9\}$ has an irreducible representation whose tensor square contains all irreducibles.

## Universal Tensor Squares for Symmetric Groups

For every positive integer *n* other than 2, 4, and 9, we prove that some irreducible complex representation of $S_{n}$ has a tensor square containing every irreducible representation. This resolves the tensor square conjecture for symmetric groups affirmatively.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026/main.pdf); the Lean below formalizes results from it.

## A Cyclic Polytabloid Proof of Saxl's Conjecture

For every staircase partition, we prove that the tensor square of the corresponding irreducible complex representation of the symmetric group contains every irreducible representation of that group. This proves Saxl's conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Cyclic-Polytabloid-Proof-of-Saxls-Conjecture-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves the universal tensor-square conjecture for symmetric groups in the stated range. For every positive integer $n\notin\{2,4,9\}$, it constructs an irreducible complex representation of $S_n$ whose tensor square contains every irreducible complex representation of $S_n$. Equivalently, all corresponding Kronecker coefficients are positive. The statement also supplies injective intertwining maps for arbitrary finite-dimensional irreducible representations.

Saxl's conjecture asserts that the tensor square of each staircase Specht module contains every irreducible representation of the corresponding symmetric group. The formalization establishes this for every $m\ge1$: if $\rho_m=(m,m-1,\ldots,1)$, then $g(\rho_m,\rho_m,\mu)>0$ for every partition $\mu$ of $m(m+1)/2$.

The stronger claim that every constituent appears in the orbit span of one prescribed tensor is not included.

## Lean: Universal irreducible tensor squares for symmetric groups

Stated in [UniversalTensorSquares.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/UniversalTensorSquares.lean).

```lean
theorem universal_tensor_square
    (n : ℕ) (hn : 0 < n) (h2 : n ≠ 2) (h4 : n ≠ 4) (h9 : n ≠ 9) :
    ∃ (lam : YoungDiagram) (hlam : lam.card = n),
      (∀ (ν : YoungDiagram) (hν : ν.card = n),
        0 < Saxl.kronecker (Saxl.canonicalTableau lam hlam)
          (Saxl.canonicalTableau lam hlam) (Saxl.canonicalTableau ν hν)) ∧
      Representation.IsIrreducible (Saxl.spechtRep (Saxl.canonicalTableau lam hlam)) ∧
      ∀ (V : Type u) [AddCommGroup V] [Module ℂ V] [Module.Finite ℂ V]
        (ρ : Representation ℂ (Equiv.Perm (Fin n)) V) [Representation.IsIrreducible ρ],
        ∃ F : Representation.IntertwiningMap ρ
          ((Saxl.spechtRep (Saxl.canonicalTableau lam hlam)).tprod
            (Saxl.spechtRep (Saxl.canonicalTableau lam hlam))),
          Function.Injective F
```

Proved in [lean/OAI/RepresentationTheory/UniversalSquare/Main.lean, line 205](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/RepresentationTheory/UniversalSquare/Main.lean#L205).

## Lean: Saxl's conjecture

Stated in [Saxl.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/Saxl.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem saxl_conjecture : SaxlConjecture
```

Proved in [lean/OAI/RepresentationTheory/Saxl/Main.lean, line 88](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/RepresentationTheory/Saxl/Main.lean#L88).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/205.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/205.md)
