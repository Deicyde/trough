---
declaration: section
origin: cited
lean: OAI.KServer.main_theorem, OAI.UniformKServer.uniform_squared_logarithmic_main
statement: formalized
proof: formalized
---

# 110. Optimal-order randomized \*k\*-server on arbitrary metrics

2 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Establishes a randomized competitive ratio $O(\log^2(k+1))$ for *k*-server on every metric space, matching the worst-case lower-bound order. One policy serves every finite oblivious request sequence, including on infinite unbounded metrics. On finite rational metrics, a uniform implementation has polynomial preprocessing and per-request bit cost in the input length and $\log(t+1)$ at request *t*, with a finite instance-dependent additive movement constant.

## Squared-logarithmic randomized k-server on arbitrary metrics

We prove that randomized *k*-server has competitive ratio $O((\log(k+1))^2)$ on every metric space against oblivious request sequences, matching the known worst-case lower bound. For each metric and initial configuration, one policy works for all finite request sequences, including on infinite and unbounded spaces. When the initial server positions are distinct, no additive term is needed.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Squared-logarithmic-randomized-k-server-on-arbitrary-metrics-September-24-2026/Squared-logarithmic-randomized-k-server-on-arbitrary-metrics-September-24-2026.pdf); the Lean below formalizes results from it.

## Uniform computation of the squared-logarithmic k-server bound

We construct a uniform randomized *k*-server algorithm on finite rational metrics with competitive ratio $O(\log^2(k+1))$ against oblivious request sequences. Preprocessing is polynomial in the input length, and per-request bit complexity is polynomial in that length and the binary request-counter length. The additive movement constant is finite and instance-dependent, but may be enormous. The construction uses the companion squared-logarithmic existence theorem.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Uniform-computation-of-the-squared-logarithmic-k-server-bound-September-24-2026/Uniform-computation-of-the-squared-logarithmic-k-server-bound-September-24-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves an $O((\log(k+1))^2)$ competitive ratio for randomized $k$-server against oblivious finite request sequences. For every $k\ge2$, every metric space containing at least $k+1$ points, and every initial configuration, one policy works for all request sequences, including in infinite and unbounded spaces.

The bound permits a configuration-dependent additive constant, which is zero when the initial server positions are distinct. The universal multiplicative constant is independent of the metric and $k$.

The formalization constructs one uniform randomized bit algorithm for $k$-server on finite rational metrics, for $2\le k<n$. Its expected movement on every oblivious finite request sequence is at most an absolute multiple of $(\log(k+1))^2$ times the offline optimum, plus a finite instance-dependent additive constant.

Preprocessing is polynomial in the encoded input length, and each request is processed in time polynomial in that length and the binary length of the request counter. Every processed request returns a legal server index. The additive movement constant is not claimed to be polynomially bounded.

## Lean: Squared-logarithmic randomized $k$-server on arbitrary metrics

Stated in [KServer.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/KServer.lean).

```lean
theorem main_theorem : MainStatement.{u}
```

Proved in [lean/OAI/Combinatorics/KServer/Main.lean, line 155](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/KServer/Main.lean#L155).

## Lean: Uniform bit algorithm for the squared-logarithmic $k$-server bound

Stated in [UniformKServer.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/UniformKServer.lean).

```lean
theorem uniform_squared_logarithmic_main : UniformAlgorithmClaim
```

Proved in [lean/OAI/Combinatorics/UniformKServer/Main.lean, line 25](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/UniformKServer/Main.lean#L25).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/110.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/110.md)
