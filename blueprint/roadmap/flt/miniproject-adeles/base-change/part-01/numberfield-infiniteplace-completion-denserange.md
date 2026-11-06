---
declaration: theorem
origin: cited
lean: NumberField.InfinitePlace.Completion.denseRange_algebraMap_subtype_pi
statement: formalized
---

# NumberField.InfinitePlace.Completion.denseRange\_algebraMap\_subtype\_pi

Let $S$ be a set of infinite places of $K$. The image of $K$ under the embedding $K\hookrightarrow (K_v)_{v\in S}; k \mapsto (k)_v$ is dense in the product topology.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $(K, v)$ denote $K$ equipped with the topology induced by the infinite place $v$. It suffices to show that the image of $K$ under the embedding $K\hookrightarrow \prod_{v\mid \infty}(K, v)$ is dense in the product topology. By a standard analytic argument, for each $v$ it is possible to select a sequence $(x_n^{(v)})_n$ with the property that $x_n^{(v)} \to 1$ in $v$'s topology, while $x_n^{(v)} \to 0$ in any other infinite place's topology. Let $(z_v)_v \in \prod_{v\mid \infty}(K, v)$. For each $v$, the sequence $y_n := \sum_{v\mid\infty} x_n^{(v)}z_v$ in $K$ converges to $z_v$ in $v$'s topology. So the embedded image of $y_n$ in $\prod_{v\mid \infty}(K, v)$ converges to $(z_v)_v$ in the product topology.

## Lean

Formalized as [`NumberField.InfinitePlace.Completion.denseRange_algebraMap_subtype_pi`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.InfinitePlace.Completion.denseRange_algebraMap_subtype_pi).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 700](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L700)
