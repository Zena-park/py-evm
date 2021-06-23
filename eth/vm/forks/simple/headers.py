from eth.vm.forks.muir_glacier.headers import (
    configure_header,
    create_header_from_parent,
    compute_muir_glacier_difficulty,
)


compute_simple_difficulty = compute_muir_glacier_difficulty

create_simple_header_from_parent = create_header_from_parent(
    compute_simple_difficulty
)
configure_simple_header = configure_header(compute_simple_difficulty)
