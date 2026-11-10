import pytest

from trough import formalization

# Cut from FormalFrontier/adic-modules and FormalFrontier/sphere-topology.
FORMAL_FRONTIER = """\
# yaml-language-server: $schema=https://raw.githubusercontent.com/mathlib-initiative/formalization.yaml/99c678e569c7c4c0772db297c5ddd5e4c9b6322e/schema/v0.4.schema.json
version: "v0.4"

project:
  name: "adic-modules"
  description: >-
    Lean theory of ideal-power torsion and adic module and ring completions,
    with quotient, tensor, finiteness and flatness interfaces.
  authors:
    - "Formal Frontier Agents"
  license: "Apache-2.0"

highlights:
  - title: "Middle exactness of completion for a Noetherian middle module"
    statement: >-
      For every ideal I of a commutative ring R and R-linear maps f : M → N
      and g : N → P, if the image of f is the kernel of g, g is surjective
      and N is Noetherian over R, then the induced maps on their inverse-limit
      I-adic completions are exact at the completion of N.
    declarations:
      - declaration: "AdicCompletion.map_exact_of_isNoetherian_middle"
        file: "AdicModules/AdicCompletion/Exactness.lean"

sources:
  - title: "Foundations of Rigid Geometry I"
    authors:
      - "Kazuhiro Fujiwara"
      - "Fumiharu Kato"
    id: "https://arxiv.org/abs/1308.4734v5"
    type: "book"
    relationship: "background"

related_formalizations:
  - id: "https://github.com/FormalFrontier/group-theory"
    relationship: "builds-on"

automation:
  methods:
    - method: "agent"
      tool_setup: >-
        Formal Frontier AI agents using Lean, Lake, Git and Hive.

status:
  scope: >-
    Uniform ideal-power torsion.
  main_results:
    - declaration: "Metric.Sphere.id_not_nullhomotopic_two"
      file: "SphereTopology/Homotopy/HomotopyGroup/SphereNontrivial.lean"
      note: "The identity of Metric.Sphere.basedSpace 1 is not homotopic to any constant map."

review:
  status: "agent-reviewed"

fidelity:
  divergences: >-
    The ideal-norm extraction removes the earlier cyclotomic specialization.
"""

# Cut from AxiomMath/CFSG.
CFSG = """\
version: "v0.4"

project:
  name: "The Classification of Finite Simple Groups"
  authors:
    - "Dean Cureton"
    - "Vasily Ilin"
  license: "Apache-2.0"

classification:
  arxiv: ["math.GR"]
  msc2020:
    - "20D05" # Finite simple groups and their classification

sources:
  - title: "CFSG Sources"
    note: "The full list of references can be found at docs/references.bib"

status:
  sorry_count: 0
  main_results:
    - declaration: "CFSGComparator.classification"
      file: "Comparator/Solution.lean"
      sorry_count: 0
      axioms: ["propext", "Classical.choice", "Quot.sound"]
      comparator_config: "comparator.json"
      literature_dependencies: []

automation:
  methods:
    - method: autonomous
      framework: "AxiomProver"

review:
  status: self-assessed
  reviewers: ["Axiom Math"]
"""

# Cut from openai/math's lean/formalization.yaml.
OPENAI = """\
version: "v0.4"

project:
  name: "OpenAI math repository"
  description: "Lean formalizations accompanying a mathematics manuscript collection."
  authors: ["OpenAI"]
  license: "Apache-2.0"

sources:
  - title: "$L_1$ Embeddings of Graphs of Bounded Treewidth"
    authors: ["OpenAI"]
    id: ../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/paper.pdf
    type: article

status:
  main_results:
    - comparator_config: ComparatorChallenges/AbhyankarSathaye.json
      declaration: OAI.AbhyankarSathaye.exists_noncoordinate_polynomial
      file: OAI/AlgebraicGeometry/AbhyankarSathaye/Counterexample.lean

automation:
  methods:
    - method: agent

review:
  status: unchecked

acknowledgements: >-
  Thank you very much to the authors of Lean 4, mathlib, and the other imported
  libraries listed above.
"""


def test_formal_frontier_highlights_and_notes_are_read():
    config = formalization.load(FORMAL_FRONTIER)
    assert config.project["name"] == "adic-modules"
    [highlight] = config.highlights
    assert highlight["title"] == "Middle exactness of completion for a Noetherian middle module"
    assert highlight["statement"].startswith("For every ideal I of a commutative ring R and R-linear maps f : M → N and g")
    assert highlight["declarations"] == [{"declaration": "AdicCompletion.map_exact_of_isNoetherian_middle",
                                          "file": "AdicModules/AdicCompletion/Exactness.lean"}]
    assert config.main_results[0]["note"].startswith("The identity of Metric.Sphere.basedSpace 1")
    assert config.related == [{"id": "https://github.com/FormalFrontier/group-theory", "relationship": "builds-on"}]
    assert formalization.text_of(config.status["scope"]) == "Uniform ideal-power torsion."


def test_keys_the_reader_does_not_name_are_kept():
    assert set(formalization.load(FORMAL_FRONTIER).extra) == {"fidelity"}
    cfsg = formalization.load(CFSG)
    assert cfsg.extra["classification"] == {"arxiv": ["math.GR"], "msc2020": ["20D05"]}
    assert cfsg.review["reviewers"] == ["Axiom Math"]
    assert cfsg.main_results[0]["comparator_config"] == "comparator.json"
    assert cfsg.main_results[0]["axioms"] == ["propext", "Classical.choice", "Quot.sound"]
    assert cfsg.highlights == []
    openai = formalization.load(OPENAI)
    assert set(openai.extra) == {"acknowledgements"}
    assert openai.review["status"] == "unchecked"
    assert openai.sources[0]["id"].startswith("../preprints/")


@pytest.mark.parametrize("cut, missing", [
    ('review:\n  status: "agent-reviewed"\n', "review.status"),
    ('automation:\n  methods:\n    - method: "agent"\n      tool_setup: >-\n'
     '        Formal Frontier AI agents using Lean, Lake, Git and Hive.\n', "automation.methods"),
    ('  license: "Apache-2.0"\n', "project.license"),
])
def test_a_missing_required_key_raises(cut, missing):
    text = FORMAL_FRONTIER.replace(cut, "")
    assert text != FORMAL_FRONTIER
    with pytest.raises(ValueError, match=missing):
        formalization.load(text)


def test_another_version_raises():
    with pytest.raises(ValueError, match="v0.3"):
        formalization.load(OPENAI.replace('version: "v0.4"', 'version: "v0.3"'))
