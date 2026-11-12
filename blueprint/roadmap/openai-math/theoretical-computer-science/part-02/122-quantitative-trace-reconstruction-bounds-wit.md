---
declaration: section
origin: cited
lean: OAI.TraceReconstruction.quantitative_sample_lower_bound, OAI.TraceReconstruction.superpolynomial_one_trace, OAI.TraceReconstruction.superpolynomial_sample_complexity
statement: formalized
proof: formalized
---

# 122. Quantitative trace-reconstruction bounds with a uniform decoder

3 manuscripts and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

At every fixed deletion probability in $(0,1)$, reconstructing an arbitrary length-*n* binary string requires $n^{\Omega(\log\log n)}$ independent traces, ruling out polynomial-sample reconstruction. A uniform decoder achieves quasipolynomial sample and running-time bounds for known fixed rational retention probabilities. When the deletion probability is at most $n^{-\varepsilon}$ for fixed *ε* > 0, both bounds become polynomial in the input and parameter encoding.

## Uniform quasipolynomial-time trace reconstruction

We give a uniform algorithm that reconstructs every binary string from independent deletion traces when its length and rational retention probability are known. For each fixed retention probability, both the number of traces and the bit complexity are quasipolynomial in the string length. More generally, we give an explicit sample bound uniform over all rational retention probabilities, with running time polynomial in the sample budget and the binary input length. If the deletion probability is at most $n^{-\varepsilon}$ for fixed *ε* > 0, the sample and running-time bounds are polynomial. Reconstruction succeeds with probability at least 2/3 for each input string.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Uniform-quasipolynomial-time-trace-reconstruction-October-5-2026/uniform-trace-reconstruction.pdf).

## A latest-anchor induction with spectrally compact masks for worst-case trace reconstruction

We give an improved worst-case sample bound for reconstructing a string from independent deletion traces, with its length and retention probability known. For each fixed retention probability, the number of traces is quasipolynomial: the logarithm of the sample budget is $O((\log n)^3(1+\log\log(2n))^6)$. If the deletion probability is at most $n^{-\varepsilon}$ for fixed *ε* > 0, polynomially many traces suffice. These bounds apply to binary strings and to strings of general symbols observed exactly. They concern sample complexity and do not assert an efficient reconstruction algorithm or matching optimality.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-latest-anchor-induction-with-spectrally-compact-masks-for-worst-case-trace-reconstruction-October-5-2026/paper.pdf).

## Quantitative lower bounds for trace reconstruction

Exact worst-case reconstruction of a binary word from independent deletion traces requires $n^{\Omega(\log\log n)}$ samples for every fixed deletion probability $q\in(0,1)$, even with unrestricted computation and any fixed positive success probability. This gives a negative answer to the polynomial-sample question for binary trace reconstruction. More generally, when $q^3\log n\to\infty$, we prove a lower bound of $n^{c\log(q^3\log n)}$ samples for every fixed $0\lt c\lt 1/(4\log2)$. Here *q* is the known deletion probability, and all logarithms are natural.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves superpolynomial sample lower bounds for exact worst-case reconstruction of binary words from independent deletion traces, with unrestricted computation and any fixed positive success probability. For every fixed deletion probability $q\in(0,1)$, sample complexity grows faster than every fixed power of the word length; the minimum total-variation distance between two one-trace laws decays faster than every inverse power.

More quantitatively, along sequences with $q^3\log n\to\infty$, the required number of samples is at least $n^{c\log(q^3\log n)}$ eventually for every fixed $0<c<1/(4\log2)$. All logarithms are natural.

## Lean: Quantitative and superpolynomial sample lower bounds for trace reconstruction

Stated in [TraceReconstruction.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/TraceReconstruction.lean).

```lean
theorem quantitative_sample_lower_bound
    (s c : ℝ) (hs : s ∈ Set.Ioc 0 1)
    (hc : c ∈ Set.Ioo 0 (1 / (4 * Real.log 2)))
    (n : ℕ → ℕ) (q : ℕ → ℝ)
    (hn : Tendsto n atTop atTop)
    (hq : ∀ k, q k ∈ Set.Ioo 0 1)
    (hscale : Tendsto (fun k => (q k) ^ 3 * Real.log (n k)) atTop atTop) :
    ∀ᶠ k in atTop,
      ENNReal.ofReal ((n k : ℝ) ^ (c * Real.log ((q k) ^ 3 * Real.log (n k)))) ≤
        sampleComplexity (n k) (q k) s
```

Proved in [lean/OAI/Probability/TraceReconstruction.lean, line 213](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/TraceReconstruction.lean#L213).

```lean
theorem superpolynomial_one_trace
    (q : ℝ) (hq : q ∈ Set.Ioo 0 1) (C : ℝ) (hC : 0 < C) :
    Tendsto (fun n : ℕ => (n : ℝ) ^ C * minTraceTV n q) atTop (𝓝 0)
```

Proved in [lean/OAI/Probability/TraceReconstruction.lean, line 332](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/TraceReconstruction.lean#L332).

```lean
theorem superpolynomial_sample_complexity
    (q : ℝ) (hq : q ∈ Set.Ioo 0 1) (s : ℝ) (hs : s ∈ Set.Ioc 0 1)
    (C : ℝ) (hC : 0 < C) :
    Tendsto
      (fun n : ℕ => sampleComplexity n q s / ENNReal.ofReal ((n : ℝ) ^ C))
      atTop (𝓝 ⊤)
```

Proved in [lean/OAI/Probability/TraceReconstruction.lean, line 378](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/TraceReconstruction.lean#L378).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/122.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/122.md)
