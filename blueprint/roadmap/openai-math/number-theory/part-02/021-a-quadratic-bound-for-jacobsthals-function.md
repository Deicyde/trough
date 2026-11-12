---
declaration: section
origin: cited
lean: OAI.Erdos970.Erdos970Final.erdos_970_quadratic, OAI.Erdos970.Erdos970Final.erdos_970_iterated_log
statement: formalized
proof: formalized
---

# 021. A quadratic bound for Jacobsthal’s function

1 manuscript and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Answers Jacobsthal's quadratic-bound question: every interval of $Ck^2$ consecutive integers contains an integer coprime to any prescribed positive integer with at most *k* distinct prime divisors, for an absolute constant *C*. The bound is uniform over prime sets and interval positions and removes the classical logarithmic loss.

## A quadratic bound for Jacobsthal's function

Let $h(k)$ be the least integer such that every interval of $h(k)$ consecutive integers contains an integer coprime to any prescribed positive integer having at most *k* distinct prime divisors. We prove $h(k)\ll k^2/(\log\log(3k))^2$, giving an affirmative answer to Jacobsthal's quadratic-bound question.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Let $h(k)$ be the least interval length that guarantees an integer coprime to any prescribed positive modulus with at most $k$ distinct prime factors. The formalization proves the paper's strengthened Jacobsthal bound $h(k)\le Ck^2/(\log\log(3k))^2$ for one absolute $C>0$ and every $k\ge1$. Intervals may begin at any signed integer. The earlier quadratic bound is also retained as a separate statement; the optimal order of growth is not determined.

## Lean: Quadratic Jacobsthal bound

Stated in [Jacobsthal.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/Jacobsthal.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem erdos_970_quadratic : NumberTheoryLean.Targets.JacobsthalQuadratic
```

Proved in [lean/OAI/NumberTheory/Jacobsthal/Conclusions/QuadraticBound.lean, line 13](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/Jacobsthal/Conclusions/QuadraticBound.lean#L13).

## Lean: Jacobsthal bound with an iterated-logarithm saving

Stated in [JacobsthalImproved.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/JacobsthalImproved.lean).

```lean
theorem erdos_970_iterated_log : NumberTheoryLean.Targets.JacobsthalIteratedLog
```

Proved in [lean/OAI/NumberTheory/Jacobsthal/Conclusions/IteratedLogBound.lean, line 59](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/Jacobsthal/Conclusions/IteratedLogBound.lean#L59).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/021.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/021.md)
