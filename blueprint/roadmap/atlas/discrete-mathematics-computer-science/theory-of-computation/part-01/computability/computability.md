---
declaration: section
origin: cited
lean: MetaMathlibExt.exists_computable_code
statement: formalized
proof: formalized
---

# Computability and undecidability: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/index.html).

Recursive and recursively enumerable predicates and their closure properties, the halting problem, Rice's and Rice–Shapiro theorems, the recursion and s-m-n theorems, enumerators, index sets such as totality, finiteness and minimal programs, and Busy Beaver functions.

## Parametrized s-m-n theorem

Let $\alpha$ be a type with a primitive recursive encoding into
the natural numbers, and for each $a \in \alpha$ let $F_a$ be a partial function from
$\mathbb{N}$ to $\mathbb{N}$, such that $(a, x) \mapsto F_a(x)$ is partial recursive. Then there
is a computable map $g$ from $\alpha$ to codes of partial recursive functions such that for all
$a \in \alpha$ and $x \in \mathbb{N}$, the partial function with code $g(a)$ agrees with $F_a$ at
$x$: both are undefined, or both are defined with the same value.

Formalized by `MetaMathlibExt.exists_computable_code`, a theorem declared in [MathlibExt/Computability/PartrecCode.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/PartrecCode.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/index.html#exists-computable-code).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Computability and undecidability](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/computability)
