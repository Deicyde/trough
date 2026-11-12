---
declaration: section
origin: cited
lean: OAI.CycleClique.thm_main
statement: formalized
proof: formalized
---

# 189. Cycle–clique Ramsey numbers

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the Erdős–Faudree–Rousseau–Schelp conjecture: $R(C_m,K_n)=(m-1)(n-1)+1$ for every $m\ge n\ge3$, except $R(C_3,K_3)=6$. This is the exact threshold forcing a red *m*-cycle or a blue *n*-clique in every red–blue coloring of a complete graph.

## Cycle--clique Ramsey numbers

We prove that $R(C_m,K_n)=(m-1)(n-1)+1$ for every pair of integers $m\ge n\ge3$ other than $(m,n)=(3,3)$, for which $R(C_3,K_3)=6$. This establishes the cycle–clique conjecture of Erdős, Faudree, Rousseau and Schelp. The proof combines expansion in a minimal counterexample with a large-clique lemma and an optimization of paths joining clique vertices. These arguments reduce the remaining cases to $3{,}099$ finite parameter-pattern instances, which are excluded by two exact implementations of proved inference rules. Complete programs and deduction traces accompany the paper.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Cycle-clique-Ramsey-numbers-September-25-2026/Cycle-clique-Ramsey-numbers-September-25-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

The cycle–clique Ramsey conjecture predicts the exact number of vertices forcing either a cycle $C_m$ or a clique $K_n$ in complementary colors. The formalization proves $R(C_m,K_n)=(m-1)(n-1)+1$ for all integers $m\ge n\ge3$ except $(m,n)=(3,3)$, where it proves $R(C_3,K_3)=6$. This is the complete parameter range of the paper's main theorem.

## Lean: Exact cycle–clique Ramsey numbers

Stated in [CycleCliqueRamsey.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CycleCliqueRamsey.lean).

```lean
theorem thm_main :
    (∀ m n : ℤ, n ≤ m → 3 ≤ n → (m, n) ≠ (3, 3) →
      (cycleCliqueRamsey m.toNat n.toNat : ℤ) = (m - 1) * (n - 1) + 1) ∧
    cycleCliqueRamsey 3 3 = 6
```

Proved in [lean/OAI/Combinatorics/Ramsey/CycleClique/MainTheorem.lean, line 23](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/Ramsey/CycleClique/MainTheorem.lean#L23).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/189.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/189.md)
