---
declaration: section
origin: cited
lean: OAI.Algorithms.SubexponentialSAT.SqrtLogSpace.exact_count_and_sat
statement: formalized
proof: formalized
---

# 378. Disproof of the Exponential Time Hypothesis

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

For every fixed $k\ge2$, a deterministic algorithm counts the satisfying assignments of a $k$-CNF with $n$ variables and $m$ clauses in time $(n+m)^{O_k(1)}2^{n/(\log n)^{1/2+o(1)}}$. This yields superlinear circuit lower bounds for a language in $\mathsf{E}^{\mathsf{NP}}$ on infinitely many input lengths.

## The Exponential Time Hypothesis is False

We give a deterministic algorithm for exactly counting the satisfying assignments of an arbitrary $k$-CNF formula. For every fixed $k\ge2$, on a formula with $n$ variables and $m$ clauses, our algorithm uses space polynomial in $n$ and $m$ and runs in time $(n+m)^{O_k(1)}2^{n/(\log n)^{1/2+o(1)}}$. Our algorithm refutes the Exponential Time Hypothesis (ETH), which postulates that deciding 3-SAT on $n$ variables requires $2^{\Omega(n)}$ time in the worst case.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

For fixed $k\ge2$, Lean proves that a deterministic machine exactly counts satisfying assignments of a canonically encoded $k$-CNF on $n$ variables in time $(L+1)^{O_k(1)}2^{O_k(n(\log\log n)^2/\sqrt{\log n})}$, where $L$ is the encoding's bit length. At every step, the machine has visited at most $(L+1)^{O_k(1)}$ tape cells in total.

For $m$ clauses, the October 25 manuscript gives the sharper time bound $(n+m)^{O_k(1)}2^{O_k(n\log\log n/\sqrt{\log n})}$. When $m\le Dn$ for fixed $D>0$, this improves to $(n+m)^{O_{k,D}(1)}2^{O_{k,D}(n/\sqrt{\log n})}$.

## Lean: Exact counting and SAT on canonical inputs in subexponential time and polynomial space

```lean
theorem exact_count_and_sat (k : ℕ) (hk : 2 ≤ k) :
    ∃ (machine : Computation.PrimitiveMachine)
      (countTape answerTape : Fin machine.tapeCount)
      (C A S : ℝ) (d e : ℕ),
      0 < C ∧ 0 < A ∧ 0 < S ∧ 0 < d ∧ 0 < e ∧
      ∀ (n : ℕ) (F : SAT.CNF (Fin n)), SAT.WidthAtMost k F →
        ∃ (time : ℕ) (final : LocatedCfg machine),
          Computation.Trace (locatedStep machine) time
            (locatedInit machine (Encoding.encodeCNF F)) final ∧
          final.config.tapes countTape =
            Turing.Tape.mk₁ ((countWord (SAT.count F)).map some) ∧
          final.config.tapes answerTape =
            Turing.Tape.mk₁ [some (decide (0 < SAT.count F))] ∧
          final.config.state = Sum.inl (decide (0 < SAT.count F)) ∧
          BinaryArithmetic.toNat (countWord (SAT.count F)) = SAT.count F ∧
          (countWord (SAT.count F)).length ≤ n + 1 ∧
          (time : ℝ) ≤ OAI.Algorithms.SubexponentialSAT.SqrtLog.Statement.runtimeBound C A d
            (Encoding.formulaBitLength F) n ∧
          ∀ (prefixSteps : ℕ) (intermediate : LocatedCfg machine),
            prefixSteps ≤ time →
            Computation.Trace (locatedStep machine) prefixSteps
              (locatedInit machine (Encoding.encodeCNF F)) intermediate →
            (visitedSpace intermediate : ℝ) ≤
              S * ((Encoding.formulaBitLength F : ℝ) + 1) ^ e
```

Stated in [SubexponentialSAT.lean, line 194](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SubexponentialSAT.lean#L194). Proved in [lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean, line 74](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean#L74). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/378.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/378.md)
