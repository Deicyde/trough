---
declaration: section
origin: cited
lean: OAI.edit_distance_main, OAI.finiteCircle_fullMain, OAI.TreeEdit.binary_lower_bound, OAI.TreeEdit.binary_torus
statement: formalized
proof: formalized
---

# 099. The sharp exponential scale of edit-distance distortion

3 manuscripts and 4 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Determines the least distortion of embedding edit distance on words of length at most *d* into real $ℓ_{1}$: it is $\exp(\Theta(\sqrt{\log d\,\log\log d}))$. Insertions, deletions and substitutions have unit cost. The constants are uniform over all finite alphabets with at least two symbols, even when the alphabet grows with *d*; binary words already force the lower bound.

## Edit Distance in l1: Matching Bounds up to Constants in the Exponent

We determine the exponential scale of the least $ℓ_{1}$ distortion of unit-cost edit distance on all strings of length at most *d*. For every sufficiently large *d*, uniformly over finite alphabets of size at least two, the distortion lies between $\exp(c\sqrt{\log d\,\log\log d})$ and $\exp(C\sqrt{\log d\,\log\log d})$ for absolute constants $c,C\gt 0$. The lower bound already holds on binary strings of one common length. Thus the order of logarithmic distortion is sharp up to absolute constants.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Edit-Distance-in-l1-Matching-Bounds-up-to-Constants-in-the-Exponent-September-27-2026/paper.pdf); the Lean below formalizes results from it.

## Finite-Circle Obstructions, Binary Codes, and Histogram Embeddings for Edit Distance

We give two finite-circle constructions of binary strings whose least $ℓ_{1}$ distortion is $\exp(\Omega(\sqrt{\log d\,\log\log d}))$, where *d* bounds their length. Both constructions supply words of one common length for every sufficiently large cap. Two direct binary coding arguments transfer the constructions with absolute distortion and logarithmic block width. We also develop the overlapping-substring method of Ostrovsky and Rabani into a complete finite histogram embedding at the same exponential scale, uniformly over all finite alphabets and all words of length at most *d*, including the empty word.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Finite-Circle-Obstructions-Binary-Codes-and-Histogram-Embeddings-for-Edit-Distance-September-27-2026/paper.pdf); the Lean below formalizes results from it.

## Tree Constructions for the l1 Distortion of Binary Edit Distance

We give two independent constructions of binary words of one length at most *d* whose ordinary edit-distance metrics require $ℓ_{1}$ distortion $\exp(\Omega(\sqrt{\log d\,\log\log d}))$ for every sufficiently large *d*. We also prove a constant-distortion binary conversion for one prescribed input length. Together with the companion upper embedding theorem, these lower bounds determine the order of logarithmic distortion uniformly over finite alphabets with at least two symbols.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Tree-Constructions-for-the-l1-Distortion-of-Binary-Edit-Distance-September-27-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization determines the exponential scale of the least $\ell_1$ distortion of unit-cost edit distance on strings of length at most $d$. For every sufficiently large $d$, uniformly over finite alphabets with at least two symbols, the distortion lies between $\exp(c\sqrt{\log d\,\log\log d})$ and $\exp(C\sqrt{\log d\,\log\log d})$ for absolute constants $c,C>0$. The lower bound has a witness consisting of binary strings of one common length, and the same scale controls the supremum over finite alphabets.

The formalization gives two finite-circle constructions of binary strings whose least $\ell_1$ distortion is at least $\exp(c\sqrt{\log d\,\log\log d})$ for all sufficiently large length caps $d$. The witnesses use strings of one common length and include the binary coding transfers with their stated uniform bounds.

It also gives a finite histogram embedding with distortion at most $\exp(C\sqrt{\log d\,\log\log d})$ for all strings of length at most $d$, uniformly over finite alphabets, including the empty string. Thus the lower and upper exponential scales agree up to absolute constants.

The formalization gives two lower-bound constructions for the $\ell_1$ distortion of ordinary edit distance on binary words. For every sufficiently large length cap $d$, each construction supplies a finite set of at least two binary words of one common length at most $d$ whose least $\ell_1$ distortion is at least $\exp(c\sqrt{\log d\,\log\log d})$ for an absolute $c>0$.

The selected statements are the binary lower bounds. The paper's constant-distortion binary conversion and the companion upper embedding theorem are outside them.

## Lean: Matching exponential-scale bounds for edit-distance distortion

```lean
theorem edit_distance_main : EditDistortion.MainClaim.{u}
```

Stated in [EditDistance.lean, line 67](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EditDistance.lean#L67). Proved in [lean/OAI/Combinatorics/EditDistance/Main.lean, line 13](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/EditDistance/Main.lean#L13).

## Lean: Finite-circle obstructions and histogram embeddings for edit distance

```lean
theorem finiteCircle_fullMain : FiniteCircle.FullMain
```

Stated in [FiniteCircle.lean, line 225](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/FiniteCircle.lean#L225). Proved in [lean/OAI/Combinatorics/FiniteCircle/Main.lean, line 139](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/FiniteCircle/Main.lean#L139).

## Lean: Binary edit-distance distortion lower bound

```lean
theorem binary_lower_bound :
    ∃ c : ℝ, 0 < c ∧ ∃ d₀ : ℕ, ∀ d : ℕ, d₀ ≤ d →
      ∃ n : ℕ, 1 ≤ n ∧ n ≤ d ∧
        ∃ W : Finset (Word Bool n), 2 ≤ W.card ∧
          growth c d ≤ binarySetDistortion W
```

Stated in [BinaryEditLower.lean, line 51](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BinaryEditLower.lean#L51). Proved in [lean/OAI/Combinatorics/BinaryEdit/BinaryLowerBound.lean, line 12](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/BinaryEdit/BinaryLowerBound.lean#L12).

## Lean: Tree-based binary edit-distance distortion lower bound

```lean
theorem binary_torus : BinaryLowerBound
```

Stated in [TreeEdit.lean, line 46](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/TreeEdit.lean#L46). Proved in [lean/OAI/Combinatorics/TreeEdit/TorusLowerBound.lean, line 106](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/TreeEdit/TorusLowerBound.lean#L106).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/099.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/099.md)
