---
declaration: section
origin: cited
lean: monotone_nat_iff_le_succ, antitone_nat_iff_succ_le, monotone_or_antitone_nat_iff
statement: formalized
proof: formalized
---

# Monotone sequences

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/ordered-sets/monotone-sequences/index.html).

## Successor criterion for monotone sequences

Let $\alpha$ be a preordered set. A sequence
$f : \mathbb{N} \to \alpha$ is monotone (that is, $f(m) \le f(n)$ whenever $m \le n$)
if and only if $f(n) \le f(n+1)$ for every $n \in \mathbb{N}$.

Formalized by `monotone_nat_iff_le_succ`, a theorem declared in [MathlibExt/Order/Monotone/Nat.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/Monotone/Nat.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/ordered-sets/monotone-sequences/index.html#monotone-nat-iff-le-succ).

## Successor criterion for antitone sequences

Let $\alpha$ be a preordered set. A sequence
$f : \mathbb{N} \to \alpha$ is antitone (that is, $f(n) \le f(m)$ whenever $m \le n$)
if and only if $f(n+1) \le f(n)$ for every $n \in \mathbb{N}$.

Formalized by `antitone_nat_iff_succ_le`, a theorem declared in [MathlibExt/Order/Monotone/Nat.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/Monotone/Nat.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/ordered-sets/monotone-sequences/index.html#antitone-nat-iff-succ-le).

## Successor criterion for monotone or antitone sequences

Let $\alpha$ be a preordered set
and let $f : \mathbb{N} \to \alpha$ be a sequence. Then $f$ is monotone ($f(m) \le f(n)$ whenever
$m \le n$) or antitone ($f(n) \le f(m)$ whenever $m \le n$) if and only if either
$f(n) \le f(n+1)$ for every $n \in \mathbb{N}$, or $f(n+1) \le f(n)$ for every $n \in \mathbb{N}$.

Formalized by `monotone_or_antitone_nat_iff`, a theorem declared in [MathlibExt/Order/Monotone/Nat.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/Monotone/Nat.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/ordered-sets/monotone-sequences/index.html#monotone-or-antitone-nat-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monotone sequences](https://deicyde.github.io/atlas-lean/roadmap/Order/ordered-sets/monotone-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Order/ordered-sets/monotone-sequences)
