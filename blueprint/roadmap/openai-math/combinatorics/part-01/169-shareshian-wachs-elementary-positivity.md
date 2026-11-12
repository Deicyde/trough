---
declaration: section
origin: cited
lean: OAI.elementaryPositivityExpansion, OAI.elementaryPositivityWitness
statement: formalized
proof: formalized
---

# 169. Shareshian–Wachs elementary positivity

1 manuscript and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the elementary-positivity part of the Shareshian–Wachs conjecture: the chromatic quasisymmetric function of every natural unit interval graph has elementary-basis coefficients in $\mathbb N[q]$. The coefficients count explicitly described permutations, giving a combinatorial explanation of positivity.

## Elementary positivity of chromatic quasisymmetric functions

We prove that the chromatic quasisymmetric function of every natural unit interval graph is elementary-positive over $\mathbb N[q]$. This resolves the elementary-positivity part of the Shareshian–Wachs conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The elementary-positivity part of the Shareshian–Wachs conjecture asks whether the chromatic quasisymmetric function of every natural unit interval graph has nonnegative coefficients in the elementary basis. The formalization proves this over $\mathbb N[q]$. It constructs an explicit elementary-basis expansion indexed by the graph's permitted nondescent permutations, with each term weighted by a nonnegative power of $q$ determined by its graph inversions. The expansion holds for every finite number of color variables.

## Lean: Elementary positivity for natural unit interval graphs

Stated in [ElementaryPositivity.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ElementaryPositivity.lean).

```lean
theorem elementaryPositivityExpansion (n : ℕ)
    (G : ElementaryPositivity.NaturalUnitIntervalGraph n) (r : ℕ) :
    G.chromatic r =
      ∑ σ : {σ : Equiv.Perm (Fin n) // G.Nondescent σ},
        MvPolynomial.C (Polynomial.X ^ G.graphInversions σ.val) *
          MvPolynomial.esymmPart (Fin r) (Polynomial ℕ)
            ((elementaryPositivityWitness n G).theta σ)
```

Proved in [lean/OAI/Combinatorics/Chromatic/Main.lean, line 35](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/Chromatic/Main.lean#L35).

```lean
def elementaryPositivityWitness (n : ℕ)
    (G : ElementaryPositivity.NaturalUnitIntervalGraph n) :
    G.PermutationWitness
```

Defined in [lean/OAI/Combinatorics/Chromatic/Main.lean, line 28](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/Chromatic/Main.lean#L28).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/169.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/169.md)
