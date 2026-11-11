---
declaration: section
origin: cited
lean: MetaMathlibExt.WeakComposition, MetaMathlibExt.SetComposition, List.partitionConjugate, MetaMathlibExt.List.IsSelfConjugate, MetaMathlibExt.Nat.partitionsInBox, MetaMathlibExt.Nat.VPartition, MetaMathlibExt.List.IsUnimodal, Nat.Partition.Dominates
statement: formalized
proof: formalized
---

# Compositions, conjugate partitions and dominance order

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/compositions-conjugate-partitions-and-dominance/index.html).

## Weak composition

Let n,k∈ℕ. A weak composition of n into
k parts is a function

a:{i∈ℕ∣ i<k}→ℕ

such that

∑ᵢ₌₀ᵏ⁻¹a(i)=n.

The values a(i) are called the parts and may be zero.
When k=0, the empty function is a weak composition
exactly when n=0.

Formalized by `MetaMathlibExt.WeakComposition`, a definition declared in [MathlibExt/Combinatorics/Fundamentals/Partitions.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Fundamentals/Partitions.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/compositions-conjugate-partitions-and-dominance/index.html#weak-composition).

## Ordered set partition

Let S be a finite set and let k∈ℕ. An
ordered set partition of S into k blocks is an ordered
tuple

(B₁,…,Bₖ)

of subsets of S such that

Bᵢ≠∅ (1≤ i≤ k),

Bᵢ∩ Bⱼ=∅
   (1≤ i,j≤ k, i≠ j),

and

⋃ᵢ₌₁ᵏ Bᵢ=S.

When k=0, the empty tuple is an ordered set partition
exactly when S=∅.

Formalized by `MetaMathlibExt.SetComposition`, a definition declared in [MathlibExt/Combinatorics/Fundamentals/Partitions.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Fundamentals/Partitions.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/compositions-conjugate-partitions-and-dominance/index.html#set-composition).

## Conjugate partition

Let $\lambda = [\lambda_1, \dots, \lambda_L]$ be a finite list of
natural numbers, with $L \ge 0$. Its conjugate $\lambda'$ is the empty list if $L = 0$, and
otherwise the list $[\lambda'_1, \dots, \lambda'_{\lambda_1}]$ of length $\lambda_1$ with
$\lambda'_j = \#\{i : 1 \le i \le L,\ \lambda_i \ge j\}$ for $1 \le j \le \lambda_1$. The length
is set by the first entry $\lambda_1$, and the entries of $\lambda'$ are weakly decreasing and at
least $1$.

When $\lambda$ is a partition, $\lambda_1 \ge \dots \ge \lambda_L \ge 1$, its first entry is its
largest part, and $\lambda'$ is the conjugate partition: its Young diagram is the transpose of the
Young diagram of $\lambda$.

Formalized by `List.partitionConjugate`, a definition declared in [MathlibExt/Combinatorics/Fundamentals/Partitions.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Fundamentals/Partitions.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/compositions-conjugate-partitions-and-dominance/index.html#partition-conjugate).

## Self-conjugate partition

Let $\lambda = [\lambda_1, \dots, \lambda_L]$ be a finite list of
natural numbers, with $L \ge 0$. Its conjugate $\lambda'$ is the empty list if $L = 0$, and
otherwise the list $[\lambda'_1, \dots, \lambda'_{\lambda_1}]$ of length $\lambda_1$ with
$\lambda'_j = \#\{i : 1 \le i \le L,\ \lambda_i \ge j\}$ for $1 \le j \le \lambda_1$. The list
$\lambda$ is self-conjugate when $\lambda' = \lambda$.

The conjugate of any list is weakly decreasing with all entries at least $1$, so a self-conjugate
list is a partition $\lambda_1 \ge \dots \ge \lambda_L \ge 1$, and for a partition the condition
says that its Young diagram equals its own transpose. The empty list is self-conjugate.

Formalized by `MetaMathlibExt.List.IsSelfConjugate`, a definition declared in [MathlibExt/Combinatorics/Fundamentals/Partitions.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Fundamentals/Partitions.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/compositions-conjugate-partitions-and-dominance/index.html#is-self-conjugate).

## Number of partitions in a box

Let $j, k, n \ge 0$ be integers. A partition of $n$ is a
finite multiset of positive integers whose sum is $n$; the empty partition is the unique partition
of $0$. Then $p(j, k, n)$ is the number of partitions of $n$ with at most $k$ parts, counted with
multiplicity, each of which is at most $j$. In particular $p(j, k, 0) = 1$ for all $j$ and $k$,
while $p(0, k, n) = p(j, 0, n) = 0$ for $n \ge 1$.

Formalized by `MetaMathlibExt.Nat.partitionsInBox`, a definition declared in [MathlibExt/Combinatorics/Fundamentals/Partitions.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Fundamentals/Partitions.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/compositions-conjugate-partitions-and-dominance/index.html#partitions-in-box).

## V-partition

Let $n \ge 0$ be an integer. A partition $\lambda$ is a finite multiset of
positive integers, and its weight $|\lambda|$ is the sum of its parts. A V-partition of weight $n$
is a triple $(c, \lambda, \mu)$ in which $c \ge 0$ is an integer, $\lambda$ and $\mu$ are
partitions all of whose parts are at most $c$, and $c + |\lambda| + |\mu| = n$.

The order of $\lambda$ and $\mu$ matters, so $(c, \lambda, \mu)$ and $(c, \mu, \lambda)$ are
distinct whenever $\lambda \ne \mu$.

Formalized by `MetaMathlibExt.Nat.VPartition`, a structure declared in [MathlibExt/Combinatorics/Fundamentals/Partitions.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Fundamentals/Partitions.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/compositions-conjugate-partitions-and-dominance/index.html#vpartition).

## Unimodal sequence

A finite list $d = [d_1, \dots, d_m]$ of natural numbers is unimodal
when $d_i \ge 1$ for every $i$ and there is an index $j$ with $1 \le j \le m$ such that
$d_1 \le d_2 \le \dots \le d_j$ and $d_j \ge d_{j+1} \ge \dots \ge d_m$. In particular a unimodal
list has $m \ge 1$, so the empty list is not unimodal; for $j = 1$ the first condition is vacuous
and for $j = m$ the second is.

Formalized by `MetaMathlibExt.List.IsUnimodal`, a definition declared in [MathlibExt/Combinatorics/Fundamentals/Partitions.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Fundamentals/Partitions.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/compositions-conjugate-partitions-and-dominance/index.html#is-unimodal).

## Dominance order on partitions

Let $n \ge 0$ be an integer. A partition of $n$ is a finite
multiset of positive integers with sum $n$; write it as the list
$\lambda = [\lambda_1, \dots, \lambda_m]$ of its parts in weakly decreasing order, so that
$\lambda_1 \ge \dots \ge \lambda_m \ge 1$ and $\lambda_1 + \dots + \lambda_m = n$, and set
$\lambda_j = 0$ for every integer $j > m$. The empty partition ($m = 0$) is the unique partition
of $0$. For partitions $\lambda$ and $\mu$ of $n$, $\lambda$ dominates $\mu$, written
$\mu \le \lambda$, if $\mu_1 + \dots + \mu_i \le \lambda_1 + \dots + \lambda_i$ for every integer
$i \ge 0$, where both sums are $0$ when $i = 0$.

Formalized by `Nat.Partition.Dominates`, a definition declared in [MathlibExt/Combinatorics/Fundamentals/Partitions.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Fundamentals/Partitions.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/compositions-conjugate-partitions-and-dominance/index.html#dominates).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Compositions, conjugate partitions and dominance order](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/compositions-conjugate-partitions-and-dominance/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/compositions-conjugate-partitions-and-dominance)
