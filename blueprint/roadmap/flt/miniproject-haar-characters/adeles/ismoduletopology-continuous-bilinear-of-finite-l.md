---
declaration: lemma
origin: cited
lean: IsModuleTopology.continuous_bilinear_of_finite_left
statement: formalized
proof: formalized
---

# IsModuleTopology.continuous\_bilinear\_of\_finite\_left

Say $R$ and $S$ are topological rings, and $S$ is an $R$-algebra, finite as an $R$-module. Assume that the topology on $S$ is the $R$-module topology. Now say $M$ is an $S$-module, and give it the induced $R$-module structure. Then the $R$-module topology and $S$-module topology on $M$ coincide.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $i:R\to S$ denote the structure map. First observe that $S$ has the $R$-module topology so the $R$-action map $R\times S\to S$ (explicitly defined by $(r,s)\mapsto i(r)s$) is continuous, and restricting to $s=1$ we deduce that $i$ is continuous.

Now let $M_R$ and $M_S$ denote $M$ with the $R$-module and $S$-module topologies respectively. It suffices to prove that the identity maps $M_R\to M_S$ and $M_S\to M_R$ are continuous. Equivalently, because the $A$-module topology on an $A$-module is the finest topology making it into a topological module, we need to prove that $M_R$ is a topological $S$-module and that $M_S$ is a topological $R$-module. We start with the latter claim.

First observe that $M_S$ is a topological $S$-module, so addition is continuous. Next note that the map $R\times M_S\to M_S$ factors through $S\times M_S$ and is hence the composite of two continuous maps and thus continuous. Hence $M_S$ is a topological $R$-module.

It thus remains to check that $M_R$ is a topological $S$-module, or equivalently that the map $S\times M_R\to M_R$ is continuous. But this map is $R$-bilinear, and by the result Module.continuous\_bilinear\_of\_finite in mathlib, any $R$-bilinear map between modules with the $R$-module topology is automatically continuous if one of the source modules is finitely-generated. The result applies because $S$ is assumed to be a finite $R$-module and the proof is complete.

## Lean

Formalized as [`IsModuleTopology.continuous_bilinear_of_finite_left`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/IsModuleTopology.continuous_bilinear_of_finite_left).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 730](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L730)
